def find_second_largest_num(lst):
    if len(lst) <= 1:
        return None
    unique_nums = set(lst[0:2])
    if len(unique_nums) < 2:
        return None
    sorted_nums = sorted(unique_nums, reverse=True)
    return sorted_nums[1]