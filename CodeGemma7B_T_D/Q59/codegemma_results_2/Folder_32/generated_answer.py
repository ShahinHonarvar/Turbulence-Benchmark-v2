def all_left_truncatable_prime(t):

    def smallest_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[42]
    truncatable_primes = []
    for n in range(2, x):
        if smallest_prime(n) and str(n) not in '0' and all((smallest_prime(int(str(n)[:i])) for i in range(1, len(str(n))))):
            truncatable_primes.append(n)
    return sorted(truncatable_primes)