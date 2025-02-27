def find_second_largest_num(lst):
    if len(lst) <= 2:
        return None
    largest = lst[0]
    second_largest = None
    for next in lst:
        if next > largest:
            second_largest = largest
            largest = next
        elif next > second_largest and next != largest:
            second_largest = next
    if second_largest == None:
        return None
    else:
        return second_largest