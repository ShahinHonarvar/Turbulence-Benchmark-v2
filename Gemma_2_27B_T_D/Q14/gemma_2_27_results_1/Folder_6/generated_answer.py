def find_second_smallest_num(nums):
    if 29 < len(nums) - 1 < 79:
        return sorted(nums[29:80])[1]
    return None