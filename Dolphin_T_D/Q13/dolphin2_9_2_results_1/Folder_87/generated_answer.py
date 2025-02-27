def find_second_largest_num(lst):
    sublist = lst[35:47]
    unique_nums = list(set(sublist))
    if len(unique_nums) < 2:
        return None
    else:
        unique_nums.sort()
        return unique_nums[-2]