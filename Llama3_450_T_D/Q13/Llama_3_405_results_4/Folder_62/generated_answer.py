def find_second_largest_num(num_list):
    nums = sorted(num_list[91:100])
    if len(nums) < 2:
        return None
    else:
        return nums[-2]