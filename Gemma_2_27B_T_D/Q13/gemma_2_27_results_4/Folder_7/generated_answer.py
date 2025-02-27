def find_second_largest_num(nums):
    if len(nums) < 264:
        return None
    sub_list = nums[661:925]
    sorted_sub_list = sorted(sub_list)
    if len(sorted_sub_list) < 2:
        return None
    return sorted_sub_list[-2]