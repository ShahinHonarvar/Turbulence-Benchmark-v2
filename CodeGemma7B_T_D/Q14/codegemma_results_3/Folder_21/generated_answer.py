def find_second_smallest_num(num_list):
    if not num_list or len(num_list) < 661 or len(num_list) > 924:
        return None
    nums = sorted(num_list[661:925])
    if len(nums) < 2:
        return None
    return nums[1]