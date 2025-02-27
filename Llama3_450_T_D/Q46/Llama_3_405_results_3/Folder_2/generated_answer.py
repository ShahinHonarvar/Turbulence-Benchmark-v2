import math

def gcf_three_nums(nums):
    nums = [nums[i] for i in [307, 920, 463]]

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    result = nums[0]
    for num in nums[1:]:
        result = gcf(result, num)
    return result