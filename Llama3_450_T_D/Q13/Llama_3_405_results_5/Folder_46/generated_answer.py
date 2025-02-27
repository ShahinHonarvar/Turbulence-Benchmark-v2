def find_second_largest_num(num_list):
    if len(num_list) < 88:
        return None
    nums = num_list[30:88]
    nums.sort(reverse=True)
    if len(nums) < 2:
        return None
    return nums[1]