def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[96]
    truncatable_primes = [str(i) for i in range(2, x + 1) if is_prime(i)]
    for i in range(len(truncatable_primes) - 1, -1, -1):
        t = truncatable_primes[i]
        n = len(t)
        if n > 2:
            if not all((is_prime(int(t[j:n - 1])) for j in range(1, n - 1))):
                truncatable_primes.pop(i)
    return sorted([int(t) for t in truncatable_primes], reverse=True)