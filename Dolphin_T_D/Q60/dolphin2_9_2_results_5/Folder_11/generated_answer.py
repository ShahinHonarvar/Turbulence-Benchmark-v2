def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = [n for n in range(2, x + 1) if is_prime(n)]
    left_right_truncatable_primes = []
    for p in primes:
        n = p
        while n != 0 and n != 2:
            if not str(n).startswith('0') and all((int(str(n)[i:j]) != 0 and is_prime(int(str(n)[i:j])) for i in range(len(str(n))) for j in range(i + 2, len(str(n)) + 1))):
                left_right_truncatable_primes.append(n)
            n = int(str(n)[1:-1])
    return sorted(list(set(left_right_truncatable_primes)))