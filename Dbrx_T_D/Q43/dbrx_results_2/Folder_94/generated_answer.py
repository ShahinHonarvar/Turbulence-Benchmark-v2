def find_primes_between_indices(numbers_list):
    prime_numbers = []
    for i in range(10, 13):
        if i < len(numbers_list) and is_prime(numbers_list[i]):
            prime_numbers.append(numbers_list[i])
    return sorted(prime_numbers)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True