def find_primes_between_indices(lst):

    def is_prime(num):
        if num in (0, 1):
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    return sorted([num for num in lst[56:58] if is_prime(num)], reverse=True)