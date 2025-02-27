def all_right_truncatable_prime(x):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i:
                i += 2
            else:
                return False
        return True
    right_truncatable_primes = []
    for n in range(2, x):
        for i in range(1, len(str(n))):
            n = int(n / 10)
            if not is_prime(n):
                break
        else:
            right_truncatable_primes.append(n)
    return sorted(right_truncatable_primes, reverse=True)