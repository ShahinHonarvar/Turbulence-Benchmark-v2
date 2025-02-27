def all_left_truncatable_prime(x):

    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if n < 2:
            return False
        while n != 0:
            if is_prime(n) and (not n % 10):
                return False
            n //= 10
        return True
    prime_list = []
    for i in range(2, x):
        if is_truncatable(i) and x > i:
            prime_list.append(i)
    prime_list.sort(reverse=True)
    return prime_list