def find_second_largest_num(num_list):
    sub_list = num_list[4:5]
    unique_nums = list(set(sub_list))
    unique_nums.sort(reverse=True)
    if len(unique_nums) < 2:
        return None
    else:
        return unique_nums[1]