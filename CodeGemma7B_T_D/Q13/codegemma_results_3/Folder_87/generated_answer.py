def find_second_largest_num(num_list):
    nums = num_list[36:47]
    if len(nums) < 2:
        return None
    nums.sort()
    return nums[-2]