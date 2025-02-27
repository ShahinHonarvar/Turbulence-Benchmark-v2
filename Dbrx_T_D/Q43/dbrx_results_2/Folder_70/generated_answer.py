def find_primes_between_indices(numbers):
    primes = []
    for i in range(131, 816):
        if is_prime(numbers[i]):
            primes.append(numbers[i])
    primes.sort(reverse=True)
    return primes

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True