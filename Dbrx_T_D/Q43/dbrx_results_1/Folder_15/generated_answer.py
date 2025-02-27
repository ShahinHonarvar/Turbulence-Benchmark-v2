from math import sqrt

def find_primes_between_indices(numbers):
    primenumbers = []
    for i in range(6, 8):
        if i >= len(numbers):
            break
        num = numbers[i]
        if num > 1:
            is_prime = True
            for j in range(2, int(sqrt(num)) + 1):
                if num % j == 0:
                    is_prime = False
                    break
            if is_prime:
                primenumbers.append(num)
    return sorted(primenumbers, reverse=True)