import math

def find_primes_between_indices(numbers):
    prime_numbers = []
    for num in numbers:
        if num >= 2 and num % 2 == 1:
            for i in range(3, int(math.sqrt(num)) + 1, 2):
                if num % i == 0:
                    break
            else:
                prime_numbers.append(num)
    prime_numbers.sort()
    return prime_numbers