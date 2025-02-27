from math import sqrt

def find_primes_between_indices(numbers):
    prime_numbers = []
    for num in numbers[87:89 + 1]:
        is_prime = True
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)
    prime_numbers.sort()
    return prime_numbers if prime_numbers else []