def find_second_largest_num(nums):
    if len(nums[4:9]) < 2:
        return None
    return sorted(nums[4:9])[-2]