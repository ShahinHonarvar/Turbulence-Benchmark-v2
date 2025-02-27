def find_second_largest_num(lst):
    if len(lst) < 3:
        return None
    subset = lst[64:67]
    largest = None
    second_largest = None
    for num in subset:
        if largest is None or num > largest:
            second_largest = largest
            largest = num
        elif largest != num and (second_largest is None or num > second_largest):
            second_largest = num
    if second_largest is None:
        return None
    return second_largest