def find_second_largest_num(nums):
    return sorted(nums[55:99], reverse=True)[1] if len(nums[55:99]) > 1 else None