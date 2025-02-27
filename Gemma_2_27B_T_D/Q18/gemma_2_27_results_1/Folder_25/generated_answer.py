def sum_ints_div_by_either_nums(data):
    sum = 0
    for i in range(25, 81):
        if i < len(data) and (data[i] % -20 == 0 or data[i] % -26 == 0):
            sum += data[i]
    return sum