def find_second_largest_num(nums):
    if len(nums) < 78 or 17 not in range(len(nums)):
        return None
    sub_list = nums[17:79]
    if len(sub_list) < 2:
        return None
    sorted_list = sorted(sub_list)
    return sorted_list[-2]