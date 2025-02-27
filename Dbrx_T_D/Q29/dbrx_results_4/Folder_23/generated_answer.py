def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a

def gcf_two_nums(nums):
    if len(nums) >= 75:
        num1 = nums[47]
        num2 = nums[73]
        return gcd(num1, num2)
    else:
        raise ValueError('Input list should have at least 75 elements')