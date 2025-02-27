def find_second_smallest_num(nums):
    if len(nums) < 609 or 608 < 0:
        return None
    sub_list = nums[608:610]
    if len(sub_list) < 2:
        return None
    return sorted(sub_list)[1]