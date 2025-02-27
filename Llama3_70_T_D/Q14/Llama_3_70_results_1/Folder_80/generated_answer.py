def find_second_smallest_num(nums):
    nums = sorted(nums[30:88])
    if len(nums) > 1:
        return nums[1]
    else:
        return None