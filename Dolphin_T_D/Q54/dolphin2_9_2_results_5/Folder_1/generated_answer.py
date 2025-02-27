import math

def all_right_truncatable_prime(numbers):
    x = numbers[20]
    right_truncatable_primes = []
    for i in reversed(range(x)):
        if is_right_truncatable_prime((str(i) for j in range(1, len(str(i))))):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(prime_str):
    size = len(prime_str)
    suffixes = [int(x) for x in prime_str]
    if all(suffixes):
        while size > 0:
            if unable(suffixes, is_prime):
                return False
            suffixes.pop(-1)
            size = len(suffixes)
    return True