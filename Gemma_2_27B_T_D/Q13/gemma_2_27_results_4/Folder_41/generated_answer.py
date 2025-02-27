def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    if nums[6] >= nums[7]:
        return nums[7]
    else:
        return nums[6]