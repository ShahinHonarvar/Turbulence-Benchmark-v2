from fractions import gcd

def gcf_three_nums(numbers):
    nums = [numbers[4], numbers[1], numbers[7]]
    factor = nums[0]
    for num in nums:
        factor = gcd(num, factor)
    return factor