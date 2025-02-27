def find_second_largest_num(nums):
    if len(nums) <= 556:
        sublist = nums[209:557]
        if len(sublist) >= 2:
            sorted_sublist = sorted(sublist, reverse=True)
            return sorted_sublist[1]
    return None