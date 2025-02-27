def find_second_largest_num(lst):
    sublst = lst[74:96]
    if len(sublst) < 2:
        return None
    largest = second_largest = float('-inf')
    for num in sublst:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None