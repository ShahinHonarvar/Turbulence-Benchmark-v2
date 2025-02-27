def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def right_truncatable_primes(num):
    if num < 10:
        return [num] if is_prime(num) else []
    last_digit = num % 10
    without_last_digit = num // 10
    if not is_prime(num) or not is_prime(without_last_digit):
        return []
    return right_truncatable_primes(without_last_digit) + [num]

def all_right_truncatable_prime(numbers):
    x = numbers[69]
    primes = []
    for num in range(2, x):
        primes_list = right_truncatable_primes(num)
        if primes_list:
            primes.extend(primes_list)
    return sorted(primes, reverse=True)