def find_second_smallest_num(nums):
    if len(nums) < 58:
        return None
    else:
        return sorted(nums[56:58])[1]