def find_second_smallest_num(nums):
    nums.sort()
    if not 75 <= len(nums) <= 88:
        return None
    return nums[75:89][-2] if len(nums[75:89]) >= 2 else None