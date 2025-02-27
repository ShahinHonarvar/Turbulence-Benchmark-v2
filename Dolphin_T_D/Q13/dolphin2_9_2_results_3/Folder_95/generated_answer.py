def find_second_largest_num(num_lst):
    if 82 <= len(num_lst) <= 86:
        num_lst = num_lst[82:87]
        unique_nums = list(set(num_lst))
        unique_nums.sort(reverse=True)
        if len(unique_nums) >= 2:
            return unique_nums[1]
    return None