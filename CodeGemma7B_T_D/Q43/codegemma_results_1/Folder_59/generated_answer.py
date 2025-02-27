def find_primes_between_indices(list_of_numbers):
    prime_numbers = []
    for i in range(5, 9):
        if is_prime(list_of_numbers[i]):
            prime_numbers.append(list_of_numbers[i])
    if prime_numbers:
        prime_numbers.sort(reverse=True)
        return prime_numbers
    else:
        return []