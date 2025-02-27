def find_second_largest_num(nums):
    if len(nums[66:94]) < 2:
        return None
    return sorted(nums[66:94])[-2]