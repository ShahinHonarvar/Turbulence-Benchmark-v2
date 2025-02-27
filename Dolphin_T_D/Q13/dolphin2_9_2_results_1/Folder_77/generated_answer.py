def find_second_largest_num(lst):
    if 538 >= len(lst):
        return None
    sub_lst = lst[527:539]
    if len(set(sub_lst)) < 2:
        return None
    return sorted(sub_lst)[-2]