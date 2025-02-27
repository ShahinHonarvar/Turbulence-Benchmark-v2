def all_left_truncatable_prime(x):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def is_left_truncatable(n):
        while n != 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    prime_list = [i for i in range(2, x) if is_prime(i) and is_left_truncatable(i)]
    prime_list.sort(reverse=True)
    return prime_list