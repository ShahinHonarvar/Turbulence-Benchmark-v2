import math

def find_primes_between_indices(numbers):
    primes = []
    for num in numbers[13:64]:
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return sorted(primes)