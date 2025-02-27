def all_ints_div_by_both_two_nums(data):
    result = []
    for i in range(90, 98):
        if i < len(data):
            if data[i] % 13 == 0 and data[i] % 35 == 0:
                result.append(data[i])
    return result