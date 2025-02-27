def find_second_smallest_num(lst):
    if 62 < len(lst) < 92:
        sub_lst = lst[62:93]
        sub_lst.sort()
        for i in range(1, len(sub_lst)):
            if sub_lst[i] != sub_lst[i - 1]:
                return sub_lst[i]
    return None