def find_second_largest_num(nums):
    if not nums or len(nums) < 22 or len(nums) > 50:
        return None
    return sorted(nums[22:51], reverse=True)[1]