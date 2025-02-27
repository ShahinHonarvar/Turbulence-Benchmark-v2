def find_second_smallest_num(nums):
    if len(nums) < 62 or 17 not in range(len(nums)) or 78 not in range(len(nums)):
        return None
    sub_list = nums[17:79]
    sorted_list = sorted(sub_list)
    if len(sorted_list) >= 2:
        return sorted_list[1]
    else:
        return None