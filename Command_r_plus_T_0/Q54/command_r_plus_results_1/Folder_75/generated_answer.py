def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def right_truncatable_primes(num):
    primes = []
    while num > 0:
        if is_prime(num):
            primes.append(num)
        num //= 10
    return primes

def all_right_truncatable_prime(numbers):
    x = numbers[41]
    truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            truncatable = right_truncatable_primes(num)
            if len(truncatable) == len(str(num)):
                truncatable_primes.append(num)
    return sorted(truncatable_primes)