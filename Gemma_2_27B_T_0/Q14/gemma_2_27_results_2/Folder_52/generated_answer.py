def find_second_smallest_num(nums):
    if len(nums) < 66 or len(nums) < 65:
        return None
    sub_list = nums[64:67]
    if len(sub_list) < 2:
        return None
    return sorted(sub_list)[1]