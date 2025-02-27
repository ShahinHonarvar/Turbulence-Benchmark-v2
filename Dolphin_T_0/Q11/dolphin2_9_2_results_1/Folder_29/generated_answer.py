def find_largest_num(lst):
    largest = None
    for i in range(59, 98):
        if largest is None or lst[i] > largest:
            largest = lst[i]
    return largest