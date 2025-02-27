def sum_in_range(input_list):
    total = 0
    for num in input_list:
        if num in range(46, 92):
            total += num
    return total if total != 0 else 0