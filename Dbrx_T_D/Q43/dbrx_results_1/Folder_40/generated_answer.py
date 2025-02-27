def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes_between_indices(numbers):
    if len(numbers) < 2:
        return []
    prime_numbers = []
    for i in range(1, 2):
        current_number = numbers[i]
        if is_prime(current_number):
            prime_numbers.append(current_number)
    return sorted(prime_numbers)