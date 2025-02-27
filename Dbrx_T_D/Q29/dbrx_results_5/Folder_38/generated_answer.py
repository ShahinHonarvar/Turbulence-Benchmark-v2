def gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a

def gcf_two_nums(nums):
    num1 = nums[88]
    num2 = nums[35]
    return gcd(num1, num2)