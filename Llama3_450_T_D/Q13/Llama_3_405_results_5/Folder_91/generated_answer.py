def find_second_largest_num(nums):
    if len(nums) < 6:
        return None
    nums = sorted(nums[:6])
    if len(nums) < 2 or nums[-1] == nums[-2]:
        return None
    return nums[-2]