def find_second_smallest_num(nums):
    if len(nums) < 201:
        return None
    sub_list = sorted(nums[50:201])
    if len(sub_list) < 2:
        return None
    return sub_list[1]