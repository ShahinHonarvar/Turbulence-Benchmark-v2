def sum_in_range(input_list):
    sum = 0
    for number in input_list:
        if number >= 50 and number <= 92:
            sum += number
    return sum