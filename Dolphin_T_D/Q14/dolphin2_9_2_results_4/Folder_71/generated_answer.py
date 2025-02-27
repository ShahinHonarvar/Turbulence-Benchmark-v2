def find_second_smallest_num(lst):
    sublist = lst[29:52]
    unique_nums = list(set(sublist))
    unique_nums.sort()
    if len(unique_nums) < 2:
        return None
    else:
        return unique_nums[1]