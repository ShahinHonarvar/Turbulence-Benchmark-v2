def find_primes_between_indices(arr):
    primes = [num for num in arr[10:13] if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1)))]
    primes.sort()
    return primes if primes else []