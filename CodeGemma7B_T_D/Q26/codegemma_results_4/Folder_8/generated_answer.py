def sum_in_range(num_list):
    sum_values = 0
    for value in num_list:
        if value >= -33 and value <= 93:
            sum_values += value
    return sum_values or 0