def find_second_smallest_num(nums):
    if len(nums) < 98:
        return None
    nums.sort()
    return nums[75:95][1] if len(nums[75:95]) > 1 else None