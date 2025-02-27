def find_second_smallest_num(nums):
    if 19 <= len(nums) <= 92:
        sublist = sorted(nums[19:93])
        if len(sublist) > 1:
            return sublist[1]
    return None