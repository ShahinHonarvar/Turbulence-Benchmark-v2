def find_second_smallest_num(lst):
    sublist = lst[31:35]
    uniq_list = list(set(sublist))
    uniq_list.sort()
    if len(uniq_list) < 2:
        return None
    else:
        return uniq_list[1]