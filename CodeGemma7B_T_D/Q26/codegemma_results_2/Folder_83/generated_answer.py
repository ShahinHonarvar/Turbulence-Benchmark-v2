def sum_in_range(list1):
    s = 0
    for num in list1:
        if num >= 2 and num <= 6:
            s += num
    return s