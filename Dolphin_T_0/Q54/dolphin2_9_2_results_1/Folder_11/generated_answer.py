def all_right_truncatable_prime(x):

    def is_truncatable_prime(n):
        if n < 10:
            return prime(n)
        for _ in range(len(str(n)) - 1):
            if not prime(int(str(n)[:-1])):
                return False
            n = int(str(n)[:-1])
        return True

    def prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return sorted([n for n in range(2, x) if is_truncatable_prime(n)])