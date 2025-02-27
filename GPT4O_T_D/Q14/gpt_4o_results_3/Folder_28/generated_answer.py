def find_second_smallest_num(nums):
    sub_list = nums[22:51]
    if len(sub_list) < 2:
        return None
    unique_nums = sorted(set(sub_list))
    return unique_nums[1] if len(unique_nums) > 1 else None