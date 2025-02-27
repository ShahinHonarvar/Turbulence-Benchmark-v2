from math import sqrt

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def remove_digits(num, start, end):
    return int(str(num)[:start] + str(num)[start + end + 1:])

def left_truncatable_primes(num):
    if num % 2 == 0 or num % 5 == 0:
        return []
    primes = [num]
    for step in range(1, len(str(num))):
        num = remove_digits(num, 0, step)
        if not is_prime(num):
            primes = []
            break
        primes.append(num)
    return primes

def right_truncatable_primes(num):
    if num % 2 == 0 or num % 5 == 0:
        return []
    primes = [num]
    for step in range(1, len(str(num))):
        num = remove_digits(num, -1, step)
        if not is_prime(num):
            primes = []
            break
        primes.append(num)
    return primes

def all_left_right_truncatable_prime(nums):
    x = nums[4]
    primes = []
    for num in range(2, x + 1):
        if is_prime(num) and num not in primes:
            left_truncatable = left_truncatable_primes(num)
            right_truncatable = right_truncatable_primes(num)
            if left_truncatable and right_truncatable:
                primes.extend(left_truncatable + right_truncatable)
    primes.sort()
    return primes