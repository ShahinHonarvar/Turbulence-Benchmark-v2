def find_second_smallest_num(nums):
    sub_nums = nums[24:88]
    if len(set(sub_nums)) < 2:
        return None
    return sorted(set(sub_nums))[1]