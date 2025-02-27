def all_right_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        for i in range(len(str(n)) - 1):
            if not is_prime(int(str(n)[i:])):
                return False
        return True
    return sorted([n for n in range(2, t[52]) if is_right_truncatable(n) and is_prime(n)], reverse=True)