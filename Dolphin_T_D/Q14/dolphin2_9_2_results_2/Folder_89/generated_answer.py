def find_second_smallest_num(nums):
    sub_list = nums[62:64]
    if sub_list:
        sorted_nums = sorted(sub_list)
        if len(sorted_nums) > 1:
            return sorted_nums[1]
    return None