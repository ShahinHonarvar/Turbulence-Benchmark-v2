def all_right_truncatable_prime(x):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        if len(str(n)) == 1:
            return is_prime(n)
        if not is_prime(n):
            return False
        return is_right_truncatable_prime(int(str(n)[:-1]))
    return sorted([n for n in range(x, 2, -1) if is_right_truncatable_prime(n)], reverse=True)