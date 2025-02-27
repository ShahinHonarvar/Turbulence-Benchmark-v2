def find_second_largest_num(nums):
    a = nums[75:86]
    if len(a) < 2:
        return None
    max_num = max(a)
    a.remove(max_num)
    return max(a) if len(a) > 0 else None