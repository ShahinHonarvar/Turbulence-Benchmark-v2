def find_primes_between_indices(arr):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    if 89 <= len(arr) < 94:
        primes = [x for x in arr[89:94] if is_prime(x)]
        return sorted(primes, reverse=True)
    else:
        return []