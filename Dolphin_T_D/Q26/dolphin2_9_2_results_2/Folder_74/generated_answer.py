def sum_in_range(input_list):
    total = 0
    for num in input_list:
        if 13 <= num <= 35:
            total += num
    return total