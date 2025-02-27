def find_second_largest_num(nums):
    return sorted(nums[66:94], reverse=True)[1] if len(nums[66:94]) > 1 else None