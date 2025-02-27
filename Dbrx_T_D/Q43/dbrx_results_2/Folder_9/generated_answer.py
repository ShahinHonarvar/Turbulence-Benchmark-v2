def find_primes_between_indices(numbers):
    prime_numbers = []
    for i in range(16, 72):
        candidate = numbers[i]
        if candidate < 2:
            continue
        is_prime = True
        for j in range(2, int(candidate ** 0.5) + 1):
            if candidate % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(candidate)
    return sorted(prime_numbers)