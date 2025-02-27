def find_second_smallest_num(nums):
    if 76 < len(nums) < 37:
        return None
    sub_nums = nums[36:77]
    if len(sub_nums) < 2:
        return None
    min_num = min(sub_nums)
    sub_nums.remove(min_num)
    return min(sub_nums) if len(sub_nums) > 0 else None