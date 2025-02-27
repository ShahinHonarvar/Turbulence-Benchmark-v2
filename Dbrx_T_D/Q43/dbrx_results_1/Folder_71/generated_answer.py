def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(input_list):
    prime_numbers = [num for num in input_list if is_prime(num)]
    if len(prime_numbers) < 57 or len(prime_numbers) < 64:
        return []
    return sorted(prime_numbers[57:65], reverse=True)