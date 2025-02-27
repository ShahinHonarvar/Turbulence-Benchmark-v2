def find_primes_between_indices(lst):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for idx in range(70, 72):
        if idx < len(lst) and is_prime(lst[idx]):
            primes.append(lst[idx])
    return sorted(primes, reverse=True)