def find_second_smallest_num(lst):
    slice_lst = lst[12:93]
    if len(slice_lst) < 2:
        return None
    slice_lst.sort()
    second_smallest = slice_lst[0]
    for i in range(1, len(slice_lst)):
        if slice_lst[i] != second_smallest:
            return second_smallest
        else:
            second_smallest = slice_lst[i]
    return None