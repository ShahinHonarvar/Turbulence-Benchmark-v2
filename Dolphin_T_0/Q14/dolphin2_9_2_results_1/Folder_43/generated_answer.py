def find_second_smallest_num(lst):
    sub_lst = lst[74:96]
    if len(sub_lst) < 2:
        return None
    sub_lst.sort()
    second_smallest = sub_lst[1]
    for num in sub_lst:
        if num != sub_lst[0] and num != second_smallest:
            second_smallest = num
        if second_smallest == sub_lst[-1]:
            return second_smallest
    return second_smallest if second_smallest != sub_lst[0] else None