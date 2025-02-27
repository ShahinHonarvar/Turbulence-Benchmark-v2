def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    nums = sorted(nums[:9])
    return nums[-2]