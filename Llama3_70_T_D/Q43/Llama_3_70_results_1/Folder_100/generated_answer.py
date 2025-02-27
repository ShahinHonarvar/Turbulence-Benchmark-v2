def find_primes_between_indices(num_list):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for i in range(25, 63):
        if i < len(num_list) and is_prime(num_list[i]):
            primes.append(num_list[i])
    return sorted(primes)