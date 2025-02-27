def find_primes_between_indices(lst):
    return sorted(list(filter(lambda num: num > 1 and all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))), lst[1:3])), reverse=True)