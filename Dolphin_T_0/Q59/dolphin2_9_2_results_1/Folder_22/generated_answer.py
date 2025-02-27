def all_left_truncatable_prime(num_tuple):
    x = num_tuple[85]

    def _is_left_truncatable_prime(n):
        if n <= 1:
            return False
        while n != 0:
            if n in _prime_set:
                n //= 10
            else:
                return False
        return True
    _prime_set = set()
    for i in range(2, x):
        if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1))):
            _prime_set.add(i)
    return sorted([i for i in _prime_set if _is_left_truncatable_prime(i)])