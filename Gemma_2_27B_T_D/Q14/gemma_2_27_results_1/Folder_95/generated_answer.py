def find_second_smallest_num(nums):
    if len(nums) < 85 or len(nums) < 75:
        return None
    sub_list = nums[75:86]
    if len(sub_list) < 2:
        return None
    return sorted(sub_list)[1]