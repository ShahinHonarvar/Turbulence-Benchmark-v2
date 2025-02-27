def all_right_truncatable_prime(t):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n == 1 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    x = t[126]
    primes = [i for i in range(2, x) if is_prime(i)]
    right_primes = []
    for p in primes[0] + primes:
        trunc = p
        while trunc > 1:
            if is_prime(trunc):
                right_primes.append(trunc)
                trunc //= 10
            else:
                break
    return sorted(list(set(right_primes)), reverse=True)