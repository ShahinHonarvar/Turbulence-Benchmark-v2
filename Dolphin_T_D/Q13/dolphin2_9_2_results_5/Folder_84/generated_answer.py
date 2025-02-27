def find_second_largest_num(nums):
    if 86 < len(nums) < 43:
        return None
    else:
        sub_nums = nums[43:87]
        if len(set(sub_nums)) < 2:
            return None
        else:
            sub_nums.sort()
            return sub_nums[-2]