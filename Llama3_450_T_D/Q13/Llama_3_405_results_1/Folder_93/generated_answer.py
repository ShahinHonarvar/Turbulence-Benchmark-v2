def find_second_largest_num(num_list):
    if len(num_list) < 96:
        return None
    nums = sorted(num_list[75:95], reverse=True)
    if len(nums) < 2:
        return None
    return nums[1]