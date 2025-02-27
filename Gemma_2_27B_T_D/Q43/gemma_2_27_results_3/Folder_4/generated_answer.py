def find_primes_between_indices(data):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    primes = []
    for i in range(24, 84):
        if is_prime(data[i]):
            primes.append(data[i])
    return sorted(primes)