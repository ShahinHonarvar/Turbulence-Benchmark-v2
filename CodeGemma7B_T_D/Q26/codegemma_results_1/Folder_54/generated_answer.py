def sum_in_range(int_list):
    sum = 0
    for number in int_list:
        if number >= -100 and number <= -55:
            sum += number
    return sum