def find_primes_between_indices(lst):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    start = 72
    end = 72
    if start < len(lst) and end < len(lst):
        for i in range(start, end + 1):
            if is_prime(lst[i]):
                primes.append(lst[i])
    return sorted(primes)