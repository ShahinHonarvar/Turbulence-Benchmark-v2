def find_primes_between_indices(lst):
    primes = [num for num in lst[70:72] if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1)))]
    return sorted(primes, reverse=True)