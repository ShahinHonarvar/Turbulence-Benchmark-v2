def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    sub_nums = nums[0:6]
    sorted_nums = sorted(sub_nums)
    return sorted_nums[-2]