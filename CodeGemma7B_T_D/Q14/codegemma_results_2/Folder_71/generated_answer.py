def find_second_smallest_num(nums):
    if len(nums[29:52]) < 2:
        return None
    nums[29:52].sort()
    return nums[29 + 1]