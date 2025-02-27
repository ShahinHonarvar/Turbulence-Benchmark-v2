def find_second_largest_num(nums):
    if len(nums) < 2 or min(nums) >= max(nums[35:50]):
        return None
    else:
        return sorted(nums[35:50], reverse=True)[1]