def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def left_truncatable_prime(num):
    if num < 10 and (not is_prime(num)):
        return False
    for i in range(1, len(str(num))):
        if not is_prime(int(str(num)[:i])) or int(str(num)[:i]) == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[74]
    truncatable_primes = []
    for num in range(2, x):
        if left_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)