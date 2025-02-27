def find_second_largest_num(nums):
    if len(nums) < 50:
        return None
    sub_nums = nums[35:50]
    if len(set(sub_nums)) == len(sub_nums):
        sorted_nums = sorted(sub_nums)
        if len(sorted_nums) >= 2:
            return sorted_nums[-2]
        else:
            return None
    else:
        return None