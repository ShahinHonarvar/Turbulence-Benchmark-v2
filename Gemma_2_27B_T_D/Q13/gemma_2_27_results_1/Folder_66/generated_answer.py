def find_second_largest_num(nums):
    if len(nums) >= 55:
        return sorted(nums[50:55])[-2]
    return None