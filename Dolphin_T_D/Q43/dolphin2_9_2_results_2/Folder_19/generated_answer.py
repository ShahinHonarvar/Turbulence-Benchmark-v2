def find_primes_between_indices(numbers):
    prime_numbers = []
    for i in range(21, 98):
        if numbers[i] > 1:
            for j in range(2, numbers[i]):
                if numbers[i] % j == 0:
                    break
            else:
                prime_numbers.append(numbers[i])
    return sorted(prime_numbers)