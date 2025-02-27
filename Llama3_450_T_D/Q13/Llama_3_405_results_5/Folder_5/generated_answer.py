def find_second_largest_num(num_list):
    if len(num_list) < 10:
        return None
    nums = num_list[8:10]
    nums.sort()
    if len(nums) < 2:
        return None
    return nums[-2]