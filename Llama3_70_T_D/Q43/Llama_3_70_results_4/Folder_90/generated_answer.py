def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(numbers):
    primes = [numbers[i] for i in range(413, 449) if is_prime(numbers[i])]
    return sorted(primes)