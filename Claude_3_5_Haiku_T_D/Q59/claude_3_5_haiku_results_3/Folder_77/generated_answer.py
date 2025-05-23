def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(num):
    if '0' in str(num):
        return False
    while num > 0:
        if not is_prime(num):
            return False
        num //= 10
    return True

def all_left_truncatable_prime(nums):
    x = nums[767]
    left_truncatable_primes = []
    for num in range(x - 1, 1, -1):
        if is_left_truncatable_prime(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)