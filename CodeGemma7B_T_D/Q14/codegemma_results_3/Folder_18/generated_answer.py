def find_second_smallest_num(nums):
    nums.sort()
    if len(nums) >= 49 and nums[30] < nums[48]:
        return nums[31]
    else:
        return None