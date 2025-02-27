def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def left_trunc(n):
    left_truncated = []
    while n:
        left_truncated.append(n)
        n //= 10
    return left_truncated

def all_left_truncatable_prime(nums):
    x = nums[20]
    left_truncatable_prime = []
    for num in nums:
        if num >= x:
            continue
        if has_zero(num):
            continue
        if is_prime(num) and all((is_prime(digit) for digit in left_trunc(num))):
            left_truncatable_prime.append(num)
    return sorted(left_truncatable_prime, reverse=True)

def has_zero(num):
    return '0' in str(num)