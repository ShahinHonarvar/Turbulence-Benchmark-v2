def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    max1 = lst[0]
    max2 = None
    for num in lst:
        if num > max1:
            max2 = max1
            max1 = num
        elif max2 is None or (num > max2 and num != max1):
            max2 = num
    return max2