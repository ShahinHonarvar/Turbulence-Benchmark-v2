def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable_primes(max_value):
    primes = []
    numbers_to_check = [2, 3, 5, 7]
    while numbers_to_check:
        num = numbers_to_check.pop(0)
        if num < max_value and is_prime(num):
            primes.append(num)
            for digit in '1379':
                numbers_to_check.append(num * 10 + int(digit))
    return primes

def all_right_truncatable_prime(numbers):
    x = numbers[33]
    return sorted(right_truncatable_primes(x))