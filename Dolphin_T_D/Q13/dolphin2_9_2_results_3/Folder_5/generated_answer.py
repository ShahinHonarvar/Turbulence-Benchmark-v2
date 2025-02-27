def find_second_largest_num(nums):
    if len(nums) < 2 or len(nums) > 2:
        return None
    if nums[8] > nums[9]:
        return nums[9]
    else:
        return nums[8]