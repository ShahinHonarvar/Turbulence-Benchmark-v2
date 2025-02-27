import math

def gcf_three_nums(nums):
    nums = [nums[92], nums[69], nums[95]]

    def calculate_gcf(nums):

        def gcf_two_nums(a, b):
            while b != 0:
                a, b = (b, a % b)
            return abs(a)
        result = nums[0]
        for num in nums[1:]:
            result = gcf_two_nums(result, num)
        return result
    return calculate_gcf(nums)