def all_left_right_truncatable_prime(tup):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        if n == 2 or n == 3 or n == 5 or (n == 7):
            return True
        if n < 10 or '0' in str(n):
            return False
        for i in range(1, len(str(n))):
            if not is_prime(int(str(n)[i:])) or not is_prime(int(str(n)[:-i])):
                return False
        return True
    x = tup[19]
    return sorted([n for n in range(2, x + 1) if is_left_right_truncatable_prime(n)])