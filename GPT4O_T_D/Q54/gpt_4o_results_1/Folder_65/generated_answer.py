def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_right_truncatable_prime(n):
    if not is_prime(n):
        return False
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_right_truncatable_prime(nums):
    if len(nums) < 33:
        return []
    x = nums[32]
    right_truncatable_primes = []
    for number in range(2, x):
        if is_right_truncatable_prime(number):
            right_truncatable_primes.append(number)
    return sorted(right_truncatable_primes)