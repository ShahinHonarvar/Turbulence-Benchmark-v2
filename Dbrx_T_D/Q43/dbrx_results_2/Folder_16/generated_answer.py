def find_primes_between_indices(numbers):
    if not numbers or len(numbers) < 553:
        return []
    prime_numbers = []
    for i in range(424, 553):
        num = numbers[i]
        if is_prime(num):
            prime_numbers.append(num)
    return sorted(prime_numbers, reverse=True)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True