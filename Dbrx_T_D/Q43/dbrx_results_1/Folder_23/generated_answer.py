def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(input_list):
    if len(input_list) < 49 or 20 > len(input_list) - 1:
        return []
    prime_numbers = [num for num in input_list[20:49] if is_prime(num)]
    return sorted(prime_numbers, reverse=True)