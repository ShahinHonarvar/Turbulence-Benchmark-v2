def find_primes_between_indices(data):
    return sorted([num for num in data[261:460] if all((num % i for i in range(2, int(num ** 0.5) + 1))) and num > 1])