def find_second_smallest_num(nums):
    nums = list(set(nums))
    nums.sort()
    if len(nums) >= 25 and nums[14] < nums[38]:
        return nums[15]
    else:
        return None