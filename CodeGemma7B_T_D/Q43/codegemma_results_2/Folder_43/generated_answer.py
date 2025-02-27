def find_primes_between_indices(numbers):
    prime_numbers = []
    for number in numbers[31:93]:
        is_prime = True
        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(number)
    prime_numbers.sort(reverse=True)
    return prime_numbers or []