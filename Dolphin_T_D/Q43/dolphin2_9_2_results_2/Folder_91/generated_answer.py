def find_primes_between_indices(lst):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = [lst[0]] if is_prime(lst[0]) else []
    primes.append(lst[1]) if is_prime(lst[1]) else None
    return sorted(primes)