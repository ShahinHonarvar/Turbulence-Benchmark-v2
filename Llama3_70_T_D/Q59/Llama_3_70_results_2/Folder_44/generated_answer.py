import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[39]
    truncatable_primes = []
    for num in range(11, x):
        if '0' in str(num):
            continue
        str_num = str(num)
        if all((is_prime(int(str_num[i:])) for i in range(len(str_num)))):
            truncatable_primes.append(num)
    return truncatable_primes