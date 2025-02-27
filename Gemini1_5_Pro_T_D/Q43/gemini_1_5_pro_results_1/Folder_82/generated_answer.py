def find_primes_between_indices(input_list):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for i in range(27, 87):
        if i < len(input_list) and is_prime(input_list[i]):
            primes.append(input_list[i])
    primes.sort(reverse=True)
    return primes