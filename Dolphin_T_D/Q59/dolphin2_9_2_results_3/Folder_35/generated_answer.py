def all_left_truncatable_prime(nums):
    x = nums[177]
    left_truncatable_primes = []
    for num in range(2, x):
        if all([is_prime(num), is_left_truncatable(num)]):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(int(n ** 0.5)) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable(n):
    if '0' in str(n):
        return False
    num = n
    while num > 0:
        num = int(str(num)[1:])
        if not is_prime(num):
            return False
    return True