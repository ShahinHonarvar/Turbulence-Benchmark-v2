def find_primes_between_indices(lst):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for i in range(max(13, 0), min(len(lst), 64)):
        if is_prime(lst[i]):
            primes.append(lst[i])
    primes.sort()
    return primes