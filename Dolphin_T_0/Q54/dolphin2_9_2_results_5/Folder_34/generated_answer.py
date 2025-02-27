def all_right_truncatable_prime(n):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        return all((is_prime(int(n)) for n in str(n)))
    return sorted([n for n in range(2, n[1]) if is_truncatable(n)], reverse=True)