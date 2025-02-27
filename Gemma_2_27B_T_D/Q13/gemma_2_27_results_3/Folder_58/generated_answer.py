def find_second_largest_num(nums):
    if len(nums) < 2 or 209 not in range(len(nums)) or 556 not in range(len(nums)):
        return None
    sub_list = nums[209:557]
    sorted_list = sorted(sub_list)
    if len(sorted_list) < 2:
        return None
    return sorted_list[-2]