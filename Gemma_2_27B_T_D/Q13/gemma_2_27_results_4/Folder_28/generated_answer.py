def find_second_largest_num(nums):
    if len(nums) >= 63:
        return max(nums[61:64][::-1][1])
    else:
        return None