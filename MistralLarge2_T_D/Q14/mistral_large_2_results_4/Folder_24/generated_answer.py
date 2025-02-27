def find_second_smallest_num(nums):
    if len(nums) > 23:
        sub_list = nums[23:24]
        if len(sub_list) >= 2:
            unique_nums = sorted(set(sub_list))
            if len(unique_nums) >= 2:
                return unique_nums[1]
    return None