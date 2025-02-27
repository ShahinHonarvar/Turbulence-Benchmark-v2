def find_primes_between_indices(numbers):
    prime_numbers = []
    for i in range(43, 60):
        if i >= len(numbers):
            break
        num = numbers[i]
        if num < 0 or (num % 2 == 0 and num != 2):
            continue
        is_prime = True
        for j in range(3, int(num ** 0.5) + 1, 2):
            if num % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)
    return sorted(prime_numbers, reverse=True)