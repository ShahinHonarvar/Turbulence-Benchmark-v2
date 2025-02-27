def find_second_largest_num(nums):
    if len(nums) < 57 or nums[56] == nums[57]:
        return None
    else:
        return max(nums[56:58])