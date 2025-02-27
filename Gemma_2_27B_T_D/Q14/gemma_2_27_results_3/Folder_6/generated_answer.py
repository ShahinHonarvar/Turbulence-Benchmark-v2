def find_second_smallest_num(nums):
    if len(nums[29:80]) < 2:
        return None
    return sorted(nums[29:80])[1]