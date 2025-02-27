def sum_in_range(input_list):
    sum = 0
    for i in input_list:
        if i >= 38 and i <= 81:
            sum += i
    return sum