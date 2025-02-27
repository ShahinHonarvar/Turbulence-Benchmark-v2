def find_second_largest_num(nums):
    if len(nums) < 3:
        return None
    nums = sorted(nums[:3])
    if nums[1] != nums[2]:
        return nums[1]
    else:
        return None