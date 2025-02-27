def find_second_smallest_num(nums):
    if len(nums[25:60]) < 2:
        return None
    return sorted(nums[25:60])[1]