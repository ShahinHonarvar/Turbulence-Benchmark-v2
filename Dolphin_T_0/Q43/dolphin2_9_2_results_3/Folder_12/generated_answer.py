def find_primes_between_indices(route):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    return sorted([x for i, x in enumerate(route) if i >= 16 and i <= 25 and is_prime(x)], reverse=True)