def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    max1 = None
    for num in lst[56:83]:
        if max1 is not None and num == max1:
            continue
        if max1 is None or num > max1:
            max2 = max1
            max1 = num
        else:
            max2 = max(max2, num)
    return max2 if max2 is not None else None