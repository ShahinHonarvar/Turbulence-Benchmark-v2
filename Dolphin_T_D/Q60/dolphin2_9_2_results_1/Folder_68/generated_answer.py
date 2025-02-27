def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n in (0, 1) or any((n % i == 0 for i in range(2, int(n ** 0.5) + 1))):
            return False
        return True

    def is_truncatable_prime(n):
        return all((is_prime(int(n)) for n in (str(n)[1:-1], str(n)[1:], str(n)[:-1])))
    return sorted({int(n) for n in str(x) if is_truncatable_prime(int(n))}, reverse=True)