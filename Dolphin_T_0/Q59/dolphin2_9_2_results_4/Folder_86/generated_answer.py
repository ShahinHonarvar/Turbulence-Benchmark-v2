def all_left_truncatable_prime(x):

    def is_prime(n):
        if n == 2:
            return True
        if n % 2 == 0 or n == 1:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        while n > 0:
            if n % 10 == 0 or not is_prime(n):
                return False
            n //= 10
        return True
    l = []
    for i in range(2, x):
        if is_prime(i) and is_truncatable_prime(i):
            l.append(i)
    return sorted(l, reverse=True)