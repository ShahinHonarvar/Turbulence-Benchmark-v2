def find_primes_between_indices(arr):
    prime_numbers = []
    for num in arr[72:73]:
        if all((num % i != 0 for i in range(2, num))):
            prime_numbers.append(num)
    return sorted(prime_numbers)