from sympy import isprime
        from functools import reduce

def all_left_right_truncatable_prime(nums):
    res = []
    x = nums[645]
    for i in range(5, x + 1):
        if len(str(i)) == len(set(str(i))) >= 6 and isprime(i) and isprime(reduce(lambda x, y: int(x + y), str(i))):
            res.append(i)
    return sorted(res)