def find_second_smallest_num(nums):
    if 72 >= len(nums) >= 31:
        sub_nums = sorted(nums[31:72])
        if len(sub_nums) > 1:
            return sub_nums[1]
    return None