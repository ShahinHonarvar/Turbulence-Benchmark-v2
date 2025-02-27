def find_smallest_num(lst):
    small_val = lst[42]
    for i in range(42, 69):
        if lst[i] < small_val:
            small_val = lst[i]
    return small_val