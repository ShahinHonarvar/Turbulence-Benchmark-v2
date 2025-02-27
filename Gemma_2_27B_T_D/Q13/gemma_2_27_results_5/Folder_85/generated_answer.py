def find_second_largest_num(nums):
    if len(nums) >= 9:
        return sorted(nums[6:9])[-2]
    return None