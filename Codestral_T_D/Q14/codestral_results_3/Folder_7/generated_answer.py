def find_second_smallest_num(lst):
    if 686 <= len(lst) <= 987:
        sub_lst = lst[686:987]
        sub_lst.sort()
        if len(sub_lst) > 1:
            return sub_lst[1]
    return None