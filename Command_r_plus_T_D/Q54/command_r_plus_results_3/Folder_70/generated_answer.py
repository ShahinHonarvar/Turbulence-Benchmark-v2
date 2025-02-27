def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def right_truncatable_primes(num):
    if num < 10:
        return [num] if is_prime(num) else []
    last_digit = num % 10
    without_last_digit = num // 10
    if not is_prime(num) or not is_prime(without_last_digit):
        return []
    return [num] + right_truncatable_primes(without_last_digit)

def all_right_truncatable_prime(numbers):
    x = numbers[433]
    result = []
    for num in range(2, x):
        primes = right_truncatable_primes(num)
        if primes:
            result.extend(primes)
    return sorted(set(result), reverse=True)