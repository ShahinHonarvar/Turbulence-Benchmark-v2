def all_right_truncatable_prime(t):

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[36]
    right_truncatable_primes = []
    for n in range(2, x):
        if is_prime(n):
            m = n
            while m:
                if not is_prime(m):
                    break
                m //= 10
            else:
                right_truncatable_primes.append(n)
    return sorted(right_truncatable_primes, reverse=True)