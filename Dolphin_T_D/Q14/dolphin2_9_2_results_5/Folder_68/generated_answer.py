def find_second_smallest_num(nums):
    if len(nums) < 9:
        return None
    nums.sort()
    return nums[1] if len(set(nums[:9])) > 1 else None