def all_right_truncatable_prime(x):

    def is_prime(n):
        if n in (0, 1):
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0:
            return False
        sq = int(n ** 0.5) + 1
        for divisor in range(3, sq, 2):
            if n % divisor == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        return all((is_prime(int(str(n)[i:])) for i in range(1, len(str(n)))))
    return sorted([i for i in range(2, x) if is_right_truncatable_prime(i)])