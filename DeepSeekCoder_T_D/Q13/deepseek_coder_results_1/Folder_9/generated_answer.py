def find_second_largest_num(nums):
    if len(nums) < 201:
        return None
    sub_list = nums[200:201]
    if len(sub_list) < 2:
        return None
    return sorted(sub_list)[-2]