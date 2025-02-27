def find_primes_between_indices(arr):
    return sorted([num for num in arr[33:60] if all((num % i != 0 for i in range(2, num)))], reverse=True)