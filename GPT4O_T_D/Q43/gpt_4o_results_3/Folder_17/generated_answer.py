def find_primes_between_indices(lst):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    if len(lst) < 16:
        return []
    primes = [n for n in lst[15:49] if is_prime(n)]
    return sorted(primes, reverse=True)