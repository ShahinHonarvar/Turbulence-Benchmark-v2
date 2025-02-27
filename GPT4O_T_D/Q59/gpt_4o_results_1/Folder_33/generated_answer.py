def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    if '0' in str(n) or not is_prime(n):
        return False
    length = len(str(n))
    for i in range(1, length):
        if not is_prime(int(str(n)[i:])):
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[945]
    left_truncatable_primes = []
    for num in range(2, x):
        if is_left_truncatable_prime(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)