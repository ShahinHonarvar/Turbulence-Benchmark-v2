def find_largest_num(lst):
    largest = float('-inf')
    for i in range(0, 6):
        if lst[i] > largest:
            largest = lst[i]
    return largest