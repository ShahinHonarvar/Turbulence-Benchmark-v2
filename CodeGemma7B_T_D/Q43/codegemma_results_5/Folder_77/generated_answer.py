def find_primes_between_indices(lst):
    primes = [num for num in lst[287:929] if all((num % i for i in range(2, int(num ** 0.5) + 1)))]
    primes.sort()
    return primes or []