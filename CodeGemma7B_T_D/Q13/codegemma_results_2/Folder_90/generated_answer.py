def find_second_largest_num(num_list):
    nums = num_list[262:747]
    sorted_nums = sorted(nums)
    if len(sorted_nums) < 2:
        return 'None'
    return sorted_nums[-2]