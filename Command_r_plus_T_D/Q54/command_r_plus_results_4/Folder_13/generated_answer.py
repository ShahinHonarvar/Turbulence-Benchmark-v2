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
    x = numbers[784]
    right_primes = []
    for num in range(2, x):
        if is_prime(num):
            truncatable_primes = right_truncatable_primes(num)
            if len(truncatable_primes) == len(str(num)):
                right_primes.extend(truncatable_primes)
    return sorted(right_primes)