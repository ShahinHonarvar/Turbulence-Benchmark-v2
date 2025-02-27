def find_primes_between_indices(arr):
    primes = [x for x in arr[14:69] if x > 1 and all((x % i != 0 for i in range(2, int(x ** 0.5) + 1)))]
    return sorted(primes, reverse=True) if primes else []