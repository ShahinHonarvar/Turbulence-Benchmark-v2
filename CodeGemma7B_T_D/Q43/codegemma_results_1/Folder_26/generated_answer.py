def find_primes_between_indices(input_list):
    prime_numbers = []
    for i in range(23, 49):
        if is_prime(input_list[i]):
            prime_numbers.append(input_list[i])
    return sorted(prime_numbers)

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True