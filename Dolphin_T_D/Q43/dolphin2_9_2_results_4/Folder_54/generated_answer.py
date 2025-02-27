def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(numbers):
    primes = []
    for number in numbers[13:64]:
        if is_prime(number):
            primes.append(number)
    return sorted(primes)