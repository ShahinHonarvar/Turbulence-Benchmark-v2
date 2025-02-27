def all_left_truncatable_prime(tup):

    def is_prime(n):
        if n == 2:
            return True
        if n < 2 or n > 10:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = tup[92]
    left_truncatable_primes = []
    for i in range(2, x):
        if '0' in str(i):
            continue
        trunctated = i
        while trunctated != 0:
            if not is_prime(trunctated):
                break
            trunctated = int(str(trunctated)[1:])
            if trunctated == 0:
                left_truncatable_primes.append(i)
    left_truncatable_primes.sort()
    return left_truncatable_primes