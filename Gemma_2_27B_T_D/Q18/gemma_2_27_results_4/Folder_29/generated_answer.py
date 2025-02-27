def sum_ints_div_by_either_nums(data):
    total = 0
    for i in range(55, 85):
        if i < len(data):
            if data[i] % -24 == 0 or data[i] % -11 == 0:
                total += data[i]
    return total