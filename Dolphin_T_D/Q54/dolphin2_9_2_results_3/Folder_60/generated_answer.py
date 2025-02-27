def all_right_truncatable_prime(tup):

    def _is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def _is_truncatable(n):
        n_str = str(n)
        for i in range(1, len(n_str)):
            if not _is_prime(int(n_str[i:])):
                return False
        return True
    x = tup[87]
    primes = []
    for num in range(2, x):
        if _is_prime(num) and _is_truncatable(num):
            primes.append(num)
    return sorted(primes, key=int)