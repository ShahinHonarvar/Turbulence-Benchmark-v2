def find_second_largest_num(nums):
    if len(nums) == 0 or len(nums) < 3:
        return None
    num_set = set(nums)
    if len(num_set) < 3:
        return None
    nums = sorted(nums)
    return nums[-3] if len(nums) >= 3 and nums[-1] != nums[-3] else None