def find_primes_between_indices(numbers):
    prime_numbers = []
    for i in range(33, 60):
        num = numbers[i]
        if num > 1:
            is_prime = True
            for j in range(2, int(num ** 0.5) + 1):
                if num % j == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_numbers.append(num)
    return sorted(prime_numbers, reverse=True)