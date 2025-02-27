def find_primes_between_indices(numbers):
    prime_numbers = []
    for i in range(61, 81):
        if numbers[i] is not None and is_prime(numbers[i]):
            prime_numbers.append(numbers[i])
    return sorted(prime_numbers, reverse=True)

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True