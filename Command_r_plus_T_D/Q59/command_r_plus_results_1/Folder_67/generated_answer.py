def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def left_truncatable_prime(num):
    if str(num).count('0') > 0:
        return False
    for i in range(len(str(num))):
        if not is_prime(int(str(num)[:i])):
            return False
    return True

def all_left_truncatable_prime(numbers):
    limit = numbers[71]
    left_truncatable_primes = []
    for num in range(limit, 0, -1):
        if left_truncatable_prime(num):
            left_truncatable_primes.append(num)
    return left_truncatable_primes