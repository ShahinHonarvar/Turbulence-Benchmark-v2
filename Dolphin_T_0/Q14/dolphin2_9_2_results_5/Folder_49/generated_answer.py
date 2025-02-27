def find_second_smallest_num(nums):
    if 200 < len(nums) < 80:
        return None
    sub_nums = nums[80:201]
    if len(sub_nums) < 2:
        return None
    min_num = min(sub_nums)
    sub_nums.remove(min_num)
    if len(sub_nums) < 2:
        return None
    second_min_num = min(sub_nums)
    return second_min_num