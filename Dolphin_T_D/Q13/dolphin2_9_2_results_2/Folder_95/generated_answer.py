def find_second_largest_num(lst):
    if not lst:
        return None
    max1 = None
    max2 = None
    for num in lst[82:87]:
        if max1 is None or num > max1:
            max2 = max1
            max1 = num
        elif max2 is None or num > max2:
            max2 = num
    return max2