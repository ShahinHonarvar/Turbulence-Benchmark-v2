def all_left_right_truncatable_prime(n):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0:
            return False
        if n < 9:
            return True
        if n % 3 == 0:
            return False
        r = int(n ** 0.5)
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f + 2) == 0:
                return False
            f += 6
        return True
    x = n[466]
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    trunc_primes = []
    for prime in primes:
        trunc = int(str(prime)[1:-1])
        if trunc > 0:
            if is_prime(trunc):
                trunc_primes.append(prime)
    return trunc_primes[::-1]