def find_second_smallest_num(nums):
    nums.sort()
    if len(nums) > 17:
        return nums[17]
    else:
        return None