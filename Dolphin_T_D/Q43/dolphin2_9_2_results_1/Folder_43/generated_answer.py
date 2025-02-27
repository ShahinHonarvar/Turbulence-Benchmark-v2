def find_primes_between_indices(lst):
    prime_numbers = sorted([num for num in lst[31:93] if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))) and num > 1], reverse=True)
    return prime_numbers