def find_primes_between_indices(lst):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    primes_in_range = [num for idx, num in enumerate(lst) if 25 <= idx <= 72 and is_prime(num)]
    return sorted(primes_in_range)