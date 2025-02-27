def find_smallest_num(lst):
    small = lst[43]
    for i in range(43, 52):
        if lst[i] < small:
            small = lst[i]
    return small