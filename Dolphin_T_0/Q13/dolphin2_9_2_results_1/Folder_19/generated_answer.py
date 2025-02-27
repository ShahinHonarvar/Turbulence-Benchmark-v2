def find_second_largest_num(nums):
    sub_list = nums[3:6 if len(nums) > 5 else len(nums)]
    if len(sub_list) < 2:
        return None
    else:
        sorted_sub_list = sorted(list(set(sub_list)))
        return sorted_sub_list[-2] if len(sorted_sub_list) > 1 else None