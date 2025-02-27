def find_largest_num(lst):
    largest = lst[13]
    for i in range(14, 69):
        if lst[i] > largest:
            largest = lst[i]
    return largest