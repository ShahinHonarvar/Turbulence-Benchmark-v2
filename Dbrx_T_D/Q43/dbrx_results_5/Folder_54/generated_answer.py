def find_primes_between_indices(numbers):
    prime_numbers = []
    for i in range(len(numbers)):
        if i < 13 or i > 63:
            continue
        if is_prime(numbers[i]):
            prime_numbers.append(numbers[i])
    return sorted(prime_numbers)

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True