def find_second_largest_num(nums):
    sub_nums = nums[30:49]
    if len(sub_nums) < 2:
        return None
    sorted_nums = sorted(sub_nums)
    return sorted_nums[-2]