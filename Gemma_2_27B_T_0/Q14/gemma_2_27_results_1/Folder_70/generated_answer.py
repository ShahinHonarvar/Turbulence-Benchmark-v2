def find_second_smallest_num(nums):
    if len(nums) < 49 or 35 < 0:
        return None
    sub_list = nums[35:50]
    if len(sub_list) < 2:
        return None
    return sorted(sub_list)[1]