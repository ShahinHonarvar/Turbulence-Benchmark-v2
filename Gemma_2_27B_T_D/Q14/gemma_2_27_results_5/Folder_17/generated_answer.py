def find_second_smallest_num(nums):
    if len(nums) < 38 or 28 not in range(len(nums)) or 38 not in range(len(nums)):
        return None
    sub_list = nums[28:39]
    sorted_list = sorted(sub_list)
    if len(sorted_list) >= 2:
        return sorted_list[1]
    else:
        return None