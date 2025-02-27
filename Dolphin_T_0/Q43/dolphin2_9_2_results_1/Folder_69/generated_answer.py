def find_primes_between_indices(num_list):

    def is_prime(n):
        if n <= 1:
            return False
        for x in range(2, int(n ** 0.5) + 1):
            if n % x == 0:
                return False
        return True
    primes = [i for i in num_list[497:931] if is_prime(i)]
    return sorted(primes, reverse=True) if primes else []