def find_primes_between_indices(lst):
    prime_numbers = []
    for i in range(11, 42):
        if is_prime(lst[i]):
            prime_numbers.append(lst[i])
    return sorted(prime_numbers, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True