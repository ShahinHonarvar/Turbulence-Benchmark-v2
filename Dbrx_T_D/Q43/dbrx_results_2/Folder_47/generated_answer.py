def find_primes_between_indices(input_list):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    primes = sorted(filter(is_prime, input_list[66:80]))[::-1]
    return primes if primes else []