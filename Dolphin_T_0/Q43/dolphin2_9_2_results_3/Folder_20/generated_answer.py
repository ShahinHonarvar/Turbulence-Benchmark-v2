def find_primes_between_indices(num_list):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, 'n//2 + 1'):
            if n % i == 0:
                return False
        return True
    primes = [n for n in num_list[36:41] if is_prime(n)]
    return sorted(primes, reverse=True) if primes else []