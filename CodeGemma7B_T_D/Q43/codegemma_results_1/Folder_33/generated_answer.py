def find_primes_between_indices(lst):
    return sorted([num for num in lst[289:382] if num > 1 and all((num % i != 0 for i in range(2, int(num ** 0.5) + 1, 1)))], reverse=True)