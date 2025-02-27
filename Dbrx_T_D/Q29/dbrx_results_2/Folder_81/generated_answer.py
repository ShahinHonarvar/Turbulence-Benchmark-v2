import math

def gcf_two_nums(nums):
    if len(nums) < 84:
        return 'Input list is too short, need at least 84 elements'
    else:
        num1 = nums[20]
        num2 = nums[83]
        max_num = max(num1, num2)
        factors = [x for x in range(1, max_num + 1) if max_num % x == 0]
        common_factors = [x for x in factors if num1 % x == 0 and num2 % x == 0]
        greatest_common_factor = max(common_factors)
        return greatest_common_factor