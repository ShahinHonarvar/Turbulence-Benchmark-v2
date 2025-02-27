def sum_odd_ints_inclusive(input_list):
    for i in range(len(input_list)):
        if i < 52 or i > 71:
            input_list[i] = 0
    return sum(input_list)