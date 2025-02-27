import math

def gcf_three_nums(nums):
    if not all((num > 0 for num in nums)) or len(nums) < 78:
        return 'Invalid input'
    num1, num2, num3 = (nums[74], nums[51], nums[27])

    def gcd(a, b):
        return a if b == 0 else gcd(b, a % b)

    def lcm(a, b):
        return math.floor(a * b / gcd(a, b))
    gcf = gcd(num1, gcd(num2, num3))
    return gcf