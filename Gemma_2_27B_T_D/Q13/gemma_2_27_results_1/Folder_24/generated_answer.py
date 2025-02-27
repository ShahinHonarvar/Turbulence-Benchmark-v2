def find_second_largest_num(nums):
    if len(nums[74:96]) < 2:
        return None
    return sorted(nums[74:96])[-2]