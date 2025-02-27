def find_primes_between_indices(numbers_list):
    prime_numbers = []
    for i in numbers_list[16:26]:
        if is_prime(i):
            prime_numbers.append(i)
    return sorted(prime_numbers, reverse=True)

def is_prime(num):
    if num < 2:
        return False
    for j in range(2, int(num ** 0.5) + 1):
        if num % j == 0:
            return False
    return True