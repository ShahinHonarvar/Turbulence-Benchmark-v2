def find_second_smallest_num(nums):
    if len(nums) < 68 or 13 not in range(len(nums)):
        return None
    sub_list = nums[13:69]
    sorted_list = sorted(sub_list)
    if len(sorted_list) < 2:
        return None
    return sorted_list[1]