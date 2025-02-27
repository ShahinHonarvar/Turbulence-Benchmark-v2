import functools

def compute_gcd(num1, num2):
    while num2:
        num1, num2 = (num2, num1 % num2)
    return num1

def gcf_three_nums(nums):
    return functools.reduce(compute_gcd, sorted(nums)[1:3] + [nums[7]], nums[7])