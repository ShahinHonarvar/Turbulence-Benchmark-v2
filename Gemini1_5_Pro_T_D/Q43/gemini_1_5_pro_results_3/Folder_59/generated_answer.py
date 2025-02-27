def find_primes_between_indices(input_list):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for i in range(min(7, len(input_list))):
        if is_prime(input_list[i]):
            primes.append(input_list[i])
    primes.sort()
    return primes