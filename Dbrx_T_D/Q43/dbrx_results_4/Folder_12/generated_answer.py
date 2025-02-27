def find_primes_between_indices(numbers):
    prime_numbers = []
    for i in range(16, 26):
        if i < 0 or i >= len(numbers):
            continue
        num = numbers[i]
        if num < 2:
            continue
        is_prime = True
        for j in range(2, int(num ** 0.5) + 1):
            if num % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)
    return sorted(prime_numbers, reverse=True)