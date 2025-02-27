def find_second_largest_num(nums):
    if len(nums[8:10]) >= 2:
        return sorted(nums[8:10])[-2]
    return None