from sympy import isprime

def all_right_truncatable_prime(nums):
    x = nums[50]
    result = []
    for num in range(1, x):
        str_num = str(num)
        if isprime(num) and isprime(int(str_num[:-1])):
            result.append(num)
    return sorted(result, reverse=True)