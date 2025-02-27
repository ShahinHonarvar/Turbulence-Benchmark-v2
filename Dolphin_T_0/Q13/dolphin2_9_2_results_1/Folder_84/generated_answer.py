def find_second_largest_num(nums):
    p = nums[43:87]
    if len(p) < 2:
        return None
    p.sort()
    return p[-2]