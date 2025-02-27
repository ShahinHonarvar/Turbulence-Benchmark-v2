def find_second_smallest_num(nums):
    if 43 <= len(nums) <= 51:
        sublist = sorted(nums[43:52])
        if len(sublist) > 1:
            return sublist[1]
    return None