def all_right_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        last = -1
        while n:
            last, n = (n % 10, n // 10)
            if last == 0 or not is_prime(n):
                return False
        return True
    x = t[767]
    primes = [i for i in range(x - 1, 1, -1) if is_prime(i) and is_right_truncatable_prime(i)]
    return primes