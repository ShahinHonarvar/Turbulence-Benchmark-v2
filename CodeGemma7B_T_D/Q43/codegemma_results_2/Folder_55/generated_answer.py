def find_primes_between_indices(arr):
    primes = []
    for i in range(2, len(arr) - 1):
        is_prime = True
        for j in range(2, int(arr[i] ** 0.5) + 1):
            if arr[i] % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(arr[i])
    primes.sort()
    return primes if primes else []