def find_second_smallest_num(nums):
    if len(nums) == 0 or len(nums) < 89:
        return None
    else:
        return sorted(nums[22:89])[1]