def find_primes_between_indices(lst):
    prime_numbers = []
    for num in lst[415:648]:
        if all((num % i != 0 for i in range(2, num))):
            prime_numbers.append(num)
    return sorted(prime_numbers)