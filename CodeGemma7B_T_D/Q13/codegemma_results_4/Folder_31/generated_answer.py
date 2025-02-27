def find_second_largest_num(num_list):
    nums = sorted(num_list, reverse=True)
    if not nums[75:89]:
        return None
    else:
        return nums[75:89][1]