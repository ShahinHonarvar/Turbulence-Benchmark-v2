def find_primes_between_indices(num_list):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    primes = [num_list[i] for i in range(45, 81) if is_prime(num_list[i])]
    return sorted(primes, reverse=True)