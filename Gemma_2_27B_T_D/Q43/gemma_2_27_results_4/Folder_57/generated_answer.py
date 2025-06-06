def find_primes_between_indices(data):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for i in range(35, 90):
        if is_prime(data[i]):
            primes.append(data[i])
    return sorted(primes, reverse=True)