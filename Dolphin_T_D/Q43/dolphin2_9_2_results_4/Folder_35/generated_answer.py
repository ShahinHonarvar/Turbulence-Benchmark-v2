def find_primes_between_indices(numbers):

    def is_prime(n):
        if n == 0 or n == 1:
            return False
        else:
            i = 2
            while i * i <= n:
                if n % i == 0:
                    return False
                i += 1
            return True
    primes = [n for n in numbers[112:362] if is_prime(n)]
    return sorted(primes, reverse=True) if primes else []