def find_primes_between_indices(lst):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    return sorted([num for idx, num in enumerate(lst) if 45 <= idx <= 80 and is_prime(num)], reverse=True)