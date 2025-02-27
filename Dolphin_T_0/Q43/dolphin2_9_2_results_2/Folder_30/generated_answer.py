def find_primes_between_indices(numbers):
    prime_numbers = []
    for i in range(61, 81):
        is_prime = True
        for j in range(2, int(numbers[i] ** 0.5) + 1):
            if numbers[i] % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(numbers[i])
    if not prime_numbers:
        return []
    else:
        return sorted(prime_numbers, reverse=True)