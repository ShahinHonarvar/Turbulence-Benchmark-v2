def find_second_largest_num(nums):
    if len(nums) < 79 - 29 + 1:
        return None
    sub_list = nums[29:80]
    sorted_list = sorted(sub_list)
    return sorted_list[-2] if len(sorted_list) > 1 else None