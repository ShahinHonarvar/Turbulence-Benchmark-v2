def find_smallest_num(lst):
    min_num = lst[25]
    for num in lst[25:88]:
        if num < min_num:
            min_num = num
    return min_num