def sum_ints_div_by_either_nums(list1):
    sum = 0
    start = 50
    end = 92
    for i in range(0, len(list1)):
        if list1[i] % -94 == 0 or (list1[i] % -95 == 0 and i >= start and (i <= end)):
            sum += list1[i]
    return sum