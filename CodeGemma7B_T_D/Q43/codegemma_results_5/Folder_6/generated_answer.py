def find_primes_between_indices(numbers):
    prime_numbers = []
    for num in numbers[89:94]:
        is_prime = True
        for factor in range(2, int(num ** 0.5) + 1):
            if num % factor == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)
    prime_numbers.sort(reverse=True)
    if prime_numbers:
        return prime_numbers
    else:
        return []