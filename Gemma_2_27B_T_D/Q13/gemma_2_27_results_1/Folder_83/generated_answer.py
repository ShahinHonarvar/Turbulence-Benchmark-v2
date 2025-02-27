def find_second_largest_num(nums):
    if len(nums[90:91 + 1]) < 2:
        return None
    return sorted(nums[90:91 + 1])[-2]