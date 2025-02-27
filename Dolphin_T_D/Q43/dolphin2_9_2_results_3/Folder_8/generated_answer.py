def find_primes_between_indices(lst):

    def is_prime(n):
        if n in (2, 3):
            return True
        if n % 2 == 0 or n == 1:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    return sorted([num for num in lst[43:77] if is_prime(num)], reverse=True)