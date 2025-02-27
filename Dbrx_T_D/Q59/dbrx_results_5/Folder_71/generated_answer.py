from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[22]
    result = []
    for num in range(10, x):
        if is_left_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)

def is_left_truncatable_prime(num):
    if num < 10:
        return isprime(num)
    else:
        while num > 0:
            num = num // 10
            if not isprime(num):
                return False
        return True