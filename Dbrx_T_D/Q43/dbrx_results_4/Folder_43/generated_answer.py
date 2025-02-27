def find_primes_between_indices(numbers):
    primes = []
    for i in range(31, 93):
        if i < 0 or i >= len(numbers):
            continue
        num = numbers[i]
        if is_prime(num):
            primes.append(num)
    primes.sort(reverse=True)
    return primes

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True