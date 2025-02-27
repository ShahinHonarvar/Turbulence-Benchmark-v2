def all_right_truncatable_prime(x):

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        return all((is_prime(int(str(n)[-i:])) for i in range(1, len(str(n)))))
    return sorted([i for i in range(2, x) if is_prime(i) and is_truncatable(i)])