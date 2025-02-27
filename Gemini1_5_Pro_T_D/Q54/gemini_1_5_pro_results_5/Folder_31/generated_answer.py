def all_right_truncatable_prime(numbers):
    x = numbers[50]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_right_truncatable_prime(num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)

def is_right_truncatable_prime(n):
    if n < 2:
        return False
    n = str(n)
    while len(n) > 0:
        if not is_prime(int(n)):
            return False
        n = n[:-1]
    return True

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True