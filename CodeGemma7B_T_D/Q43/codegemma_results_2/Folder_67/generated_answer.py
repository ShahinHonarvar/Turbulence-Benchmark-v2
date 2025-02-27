def find_primes_between_indices(lst):
    return sorted([num for num in lst[17:79 + 1] if all((num % i for i in range(2, int(num ** 0.5) + 1)))], reverse=True)