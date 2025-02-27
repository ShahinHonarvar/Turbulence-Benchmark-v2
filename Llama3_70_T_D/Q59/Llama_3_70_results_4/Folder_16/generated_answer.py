def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable(n):
    num_str = str(n)
    for i in range(len(num_str)):
        if not is_prime(int(num_str[i:])):
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[792]
    left_truncatable_primes = []
    for i in range(2, x):
        if '0' not in str(i) and is_prime(i) and left_truncatable(i):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)