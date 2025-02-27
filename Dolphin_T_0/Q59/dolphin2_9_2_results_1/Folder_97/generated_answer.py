def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[645]
    trunc_primes = []
    for n in range(2, x):
        if '0' not in str(n) and is_prime(n):
            trunc = n
            while trunc > 1:
                if not is_prime(int(str(trunc)[1:])):
                    break
                trunc = int(str(trunc)[1:])
            else:
                trunc_primes.append(n)
    return sorted(trunc_primes)