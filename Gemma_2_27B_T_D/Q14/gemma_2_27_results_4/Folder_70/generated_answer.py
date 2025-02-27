def find_second_smallest_num(nums):
    if len(nums) < 49:
        return None
    sub_list = nums[35:50]
    sorted_list = sorted(sub_list)
    if len(sorted_list) >= 2:
        return sorted_list[1]
    else:
        return None