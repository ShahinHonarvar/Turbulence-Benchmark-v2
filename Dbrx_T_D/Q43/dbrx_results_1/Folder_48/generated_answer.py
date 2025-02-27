def find_primes_between_indices(numbers):
    prime_numbers = []
    for i in range(len(numbers)):
        if i < 261 or i > 459:
            continue
        if is_prime(numbers[i]):
            prime_numbers.append(numbers[i])
    prime_numbers.sort()
    return prime_numbers

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True