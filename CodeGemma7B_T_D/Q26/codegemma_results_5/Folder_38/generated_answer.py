def sum_in_range(input_list):
    sum_value = 0
    for item in input_list:
        if 44 <= item <= 67:
            sum_value += item
    return sum_value if sum_value else 0