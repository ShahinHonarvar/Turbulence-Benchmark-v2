def find_second_smallest_num(num_list):
    if not num_list or len(num_list) < 44:
        return None
    nums = sorted(num_list[43:52])
    if len(nums) >= 2:
        return nums[1]
    else:
        return None