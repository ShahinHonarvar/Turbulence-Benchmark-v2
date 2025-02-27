def find_second_largest_num(nums):
    if len(nums) < 49 or 35 not in range(len(nums)) or 49 not in range(len(nums)):
        return None
    sub_list = nums[35:50]
    sorted_list = sorted(sub_list)
    if len(sorted_list) < 2:
        return None
    return sorted_list[-2]