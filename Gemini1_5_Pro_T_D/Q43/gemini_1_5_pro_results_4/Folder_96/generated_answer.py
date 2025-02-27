def find_primes_between_indices(input_list):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for i in range(max(32, 0), min(len(input_list), 36)):
        if is_prime(input_list[i]):
            primes.append(input_list[i])
    return sorted(primes)