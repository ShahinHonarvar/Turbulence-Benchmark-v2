def find_second_smallest_num(nums):
    if len(nums) < 20 or len(nums) < 93:
        return None
    sub_list = nums[19:93]
    sorted_sub_list = sorted(sub_list)
    return sorted_sub_list[1]