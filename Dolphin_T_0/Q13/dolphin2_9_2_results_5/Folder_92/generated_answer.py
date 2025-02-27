def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    max1, max2 = (None, None)
    for num in lst:
        if max1 is None or num > max1:
            max1, max2 = (num, max1)
        elif max2 is None or (num > max2 and num < max1):
            max2 = num
    return max2