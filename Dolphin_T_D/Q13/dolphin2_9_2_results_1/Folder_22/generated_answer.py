def find_second_largest_num(nums):
    if 200 < len(nums) < 40:
        return None
    sub_nums = nums[40:201]
    if len(sub_nums) < 2:
        return None
    max_num = max(sub_nums)
    sub_nums.remove(max_num)
    second_max_num = max(sub_nums)
    return second_max_num