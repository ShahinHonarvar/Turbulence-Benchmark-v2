def sum_in_range(input_list):
    total = 0
    for i in input_list:
        if 3 <= i <= 8:
            total += i
    return total