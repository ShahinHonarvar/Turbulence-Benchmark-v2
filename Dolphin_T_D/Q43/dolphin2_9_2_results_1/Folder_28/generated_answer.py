def find_primes_between_indices(lst):
    prime_numbers = []
    for num in lst[38:55]:
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            prime_numbers.append(num)
    return sorted(prime_numbers, reverse=True)