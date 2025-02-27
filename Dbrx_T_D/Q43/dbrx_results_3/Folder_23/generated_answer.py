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
    primes = []
    for i in range(min(len(lst), 20), min(len(lst), 49)):
        if is_prime(abs(lst[i])):
            primes.append(lst[i])
    return sorted(primes, reverse=True)