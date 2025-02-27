def find_primes_between_indices(lst):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        max_divisor = int(n ** 0.5) + 1
        for d in range(3, max_divisor, 2):
            if n % d == 0:
                return False
        return True
    primes = [lst[i] for i in range(10, 12) if is_prime(lst[i])]
    return sorted(primes)