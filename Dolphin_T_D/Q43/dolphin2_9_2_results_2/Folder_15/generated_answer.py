def find_primes_between_indices(lst):
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in lst[6:8]:
        if is_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)