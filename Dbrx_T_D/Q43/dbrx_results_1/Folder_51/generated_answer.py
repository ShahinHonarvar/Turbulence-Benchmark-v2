def find_primes_between_indices(numbers):
    prime_numbers = []
    for num in numbers[14:69]:
        if num > 1:
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_numbers.append(num)
    return sorted(prime_numbers, reverse=True)