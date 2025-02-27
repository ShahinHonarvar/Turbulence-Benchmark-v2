def all_left_truncatable_prime(lst):

    def _is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = lst[618]
    left_truncatable_primes = []
    for n in range(2, x):
        if _is_prime(n):
            str_n = str(n)
            if '0' not in str_n:
                trunc = str_n
                while True:
                    if not _is_prime(int(trunc)):
                        break
                    trunc = trunc[1:]
                    if len(trunc) == 0:
                        left_truncatable_primes.append(n)
                        break
    return sorted(left_truncatable_primes)