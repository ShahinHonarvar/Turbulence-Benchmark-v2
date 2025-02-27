def find_second_largest_num(nums):
    if len(nums) < 39:
        return None
    sub_list = nums[59:98]
    sorted_sub_list = sorted(sub_list)
    return sorted_sub_list[-2]