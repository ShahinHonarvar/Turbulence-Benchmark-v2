def find_second_largest_num(lst):
    second_largest = None
    for i in range(1, 9):
        if lst[i] != max(lst[:8]):
            second_largest = max(lst[:8])
            break
    return second_largest