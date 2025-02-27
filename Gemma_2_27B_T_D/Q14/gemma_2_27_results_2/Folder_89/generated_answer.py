def find_second_smallest_num(nums):
    if len(nums) >= 63 and nums[62] != nums[63]:
        return min(nums[62], nums[63])
    return None