def find_primes_between_indices(lst):

    def is_prime(x):
        if x < 2:
            return False
        if x == 2:
            return True
        if x % 2 == 0:
            return False
        for i in range(3, int(x ** 0.5) + 1, 2):
            if x % i == 0:
                return False
        return True
    return sorted([x for x in lst[16:26] if is_prime(x)], reverse=True)