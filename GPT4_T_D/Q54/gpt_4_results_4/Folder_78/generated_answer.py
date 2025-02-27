from sympy import isprime

def is_right_truncatable_prime(n):
    str_num = str(n)
    for i in range(len(str_num)):
        if not isprime(int(str_num[i:])):
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[23]
    primes = []
    for num in range(2, x):
        if is_right_truncatable_prime(num):
            primes.append(num)
    return sorted(primes)