def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a

def gcf_two_nums(nums):
    num1 = nums[51]
    num2 = nums[27]
    return gcd(num1, num2)