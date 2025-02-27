def sum_in_range(num_list):
    sum = 0
    for number in num_list:
        if number >= 1 and number <= 8:
            sum += number
    return sum