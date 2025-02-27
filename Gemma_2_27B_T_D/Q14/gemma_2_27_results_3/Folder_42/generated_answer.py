def find_second_smallest_num(nums):
    if len(nums) < 2 or 21 >= len(nums) or 97 >= len(nums):
        return None
    sub_list = nums[21:98]
    sorted_list = sorted(sub_list)
    if len(sorted_list) < 2:
        return None
    return sorted_list[1]