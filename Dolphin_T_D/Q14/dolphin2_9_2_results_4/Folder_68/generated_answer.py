def find_second_smallest_num(nums):
    if len(nums) <= 1:
        return None
    elif len(nums) > 9:
        nums = nums[:9]
    min_ = min(nums)
    nums.remove(min_)
    if len(nums) == 0:
        return None
    else:
        return min(nums)