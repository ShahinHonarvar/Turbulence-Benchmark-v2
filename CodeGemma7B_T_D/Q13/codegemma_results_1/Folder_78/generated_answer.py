def find_second_largest_num(nums):
    if len(nums[43:52]) < 2:
        return None
    else:
        nums[43:52].sort(reverse=True)
        return nums[44]