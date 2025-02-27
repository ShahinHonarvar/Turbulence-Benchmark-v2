def find_primes_between_indices(lst):

    def is_prime(n):
        if n < 2:
            return False
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True
    return sorted([lst[i] for i in range(167, 786) if is_prime(lst[i])], reverse=True)