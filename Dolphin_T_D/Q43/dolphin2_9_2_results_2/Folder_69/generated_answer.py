def find_primes_between_indices(lst):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    primes = [x for x in lst[497:931] if is_prime(x)]
    return sorted(primes, reverse=True) if primes else []