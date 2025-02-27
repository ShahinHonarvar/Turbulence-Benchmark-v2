def find_second_largest_num(nums):
    if len(nums) < 5:
        return None
    else:
        return sorted(nums[4:5])[0]