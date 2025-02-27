def find_primes_between_indices(numbers):
    prime_numbers = []
    for i in range(len(numbers)):
        if i >= 35 and i <= 89:
            is_prime = True
            for j in range(2, int(numbers[i] ** 0.5) + 1):
                if numbers[i] % j == 0:
                    is_prime = False
                    break
            if is_prime and numbers[i] > 1:
                prime_numbers.append(numbers[i])
    return sorted(prime_numbers, reverse=True)