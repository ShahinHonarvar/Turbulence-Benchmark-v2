def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(numbers):
    if len(numbers) < 77:
        relevant_numbers = numbers[55:]
    else:
        relevant_numbers = numbers[55:77]
    primes = [num for num in relevant_numbers if is_prime(num)]
    return sorted(primes)