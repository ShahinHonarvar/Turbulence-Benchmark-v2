def find_second_largest_num(nums):
    if len(nums) < 88:
        return None
    else:
        sliced_nums = nums[75:89]
        if len(set(sliced_nums)) < 2:
            return None
        else:
            sorted_nums = sorted(sliced_nums)
            return sorted_nums[-2]