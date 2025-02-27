def find_second_smallest_num(nums):
    if len(nums) < 2 or 987 >= len(nums) or 686 < 0:
        return None
    sub_list = nums[686:988]
    sorted_sub_list = sorted(sub_list)
    if len(sorted_sub_list) < 2:
        return None
    return sorted_sub_list[1]