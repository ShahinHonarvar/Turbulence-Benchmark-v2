def find_second_smallest_num(nums):
    if 62 <= len(nums) <= 92:
        sublist = sorted(nums[61:92])
        if len(sublist) >= 2:
            return sublist[1]
    return None