def find_second_largest_num(num_list):
    if len(num_list) < 49:
        return None
    nums = sorted(num_list[30:49], reverse=True)
    if len(nums) < 2:
        return None
    return nums[1]