def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    largest = second_largest = None
    for i in range(min(len(lst), 11)):
        if lst[i] > largest:
            second_largest = largest
            largest = lst[i]
        elif second_largest is None or lst[i] > second_largest:
            second_largest = lst[i]
    return second_largest