def find_second_largest_num(nums):
    if len(nums[56:58]) < 2:
        return None
    return sorted(nums[56:58])[-2]