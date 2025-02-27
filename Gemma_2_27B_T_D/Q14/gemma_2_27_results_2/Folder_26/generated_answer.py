def find_second_smallest_num(nums):
    if len(nums) < 17 or 78 >= len(nums):
        return None
    sub_list = nums[62:79]
    if len(set(sub_list)) < 2:
        return None
    return sorted(set(sub_list))[1]