def all_right_truncatable_prime(numbers):
    x = numbers[945]
    right_truncatable_primes = []
    for num in range(2, x):
        if all_right_truncations_are_prime(num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)

def all_right_truncations_are_prime(num):
    if num < 2:
        return False
    while num > 0:
        if not is_prime(num):
            return False
        num //= 10
    return True

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True