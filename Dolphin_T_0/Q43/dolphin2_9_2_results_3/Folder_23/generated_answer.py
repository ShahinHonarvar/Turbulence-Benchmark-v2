def find_primes_between_indices(lst):

    def is_prime(n):
        if n == 2:
            return True
        if n % 2 == 0 or n < 2:
            return False
        sqr = int(n ** 0.5) + 1
        for divisor in range(3, sqr, 2):
            if n % divisor == 0:
                return False
        return True
    return sorted([num for num in lst[20:49] if is_prime(num)], reverse=True)