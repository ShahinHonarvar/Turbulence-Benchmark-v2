def find_second_largest_num(lst):
    if len(lst) < 7:
        return None
    sorted_nums = sorted(lst)
    return sorted_nums[5] if sorted_nums[5] < sorted_nums[6] else sorted_nums[4]