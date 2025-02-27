def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    else:
        sorted_nums = sorted(nums[:3])
        return sorted_nums[1]