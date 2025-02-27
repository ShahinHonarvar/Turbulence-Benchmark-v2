def find_second_smallest_num(nums):
    if 56 <= len(nums) <= 66:
        sublist = sorted(nums[56:67])
        if len(sublist) > 1:
            return sublist[1]
    return None