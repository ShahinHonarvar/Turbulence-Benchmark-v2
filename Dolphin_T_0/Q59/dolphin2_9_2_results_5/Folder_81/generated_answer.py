def all_left_truncatable_prime(t):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if n == 2 or n == 3 or n == 5 or (n == 7):
            return True
        for i in range(1, len(str(n))):
            if str(n)[i] == '0' or not is_prime(int(str(n)[i:])):
                return False
        return True
    x = t[98]
    return sorted([i for i in range(2, x) if is_truncatable_prime(i)])