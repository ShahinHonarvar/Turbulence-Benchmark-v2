def find_second_largest_num(nums):
    if len(nums) > 78:
        sublist = sorted(nums[17:79], reverse=True)
        if len(sublist) > 1:
            return sublist[1]
    return None