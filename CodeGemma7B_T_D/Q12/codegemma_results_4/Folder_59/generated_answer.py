def find_smallest_num(lst):
    smallest_num = float('inf')
    for i in range(0, 9):
        if lst[i] < smallest_num:
            smallest_num = lst[i]
    return smallest_num