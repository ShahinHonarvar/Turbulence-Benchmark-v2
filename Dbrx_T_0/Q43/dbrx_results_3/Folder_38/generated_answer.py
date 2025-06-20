def find_primes_between_indices(numbers):
    primes = []
    for i in range(len(numbers)):
        if i >= 55 and i <= 87:
            if is_prime(numbers[i]):
                primes.append(numbers[i])
    primes.sort()
    return primes

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True