def find_second_largest_num(nums):
    if len(nums) < 8:
        return None
    sub_nums = nums[:8]
    if len(set(sub_nums)) != len(sub_nums):
        return None
    sorted_nums = sorted(sub_nums)
    return sorted_nums[-2]