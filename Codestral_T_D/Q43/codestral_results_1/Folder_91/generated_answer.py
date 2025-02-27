def find_primes_between_indices(lst):

    def is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    start, end = (lst[0], lst[1])
    primes = [num for num in range(start, end + 1) if is_prime(num)]
    return sorted(primes)