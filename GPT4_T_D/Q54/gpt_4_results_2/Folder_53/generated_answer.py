from sympy import isprime

def all_right_truncatable_prime(nums):
    x = nums[86]
    nums = [str(n) for n in range(2, x)]
    trunc_primes = [int(num) for num in nums if is_right_truncatable_prime(num)]
    trunc_primes.sort(reverse=True)
    return trunc_primes

def is_right_truncatable_prime(num):
    while num:
        if not isprime(int(num)):
            return False
        num = num[:-1]
    return True