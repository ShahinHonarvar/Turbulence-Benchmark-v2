def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n == 2:
            return True
        if n % 2 < 1:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i < 1:
                return False
        return True

    def is_truncatable_prime(n):
        return all((is_prime(int(str(n)[i:j])) for i in range(len(str(n))) for j in range(i + 1, len(str(n)) + 1)))
    return sorted([i for i in range(2, a + 1) if is_truncatable_prime(i)], reverse=True)