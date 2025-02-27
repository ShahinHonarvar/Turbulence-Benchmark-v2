def find_second_smallest_num(nums):
    if len(nums[29:94]) < 2:
        return None
    return sorted(nums[29:94])[1]