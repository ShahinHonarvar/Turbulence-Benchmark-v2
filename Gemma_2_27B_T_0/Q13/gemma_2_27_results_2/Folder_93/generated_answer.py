def find_second_largest_num(nums):
    if len(nums) < 94:
        return None
    sub_list = nums[75:95]
    if len(sub_list) < 2:
        return None
    return sorted(sub_list)[-2]