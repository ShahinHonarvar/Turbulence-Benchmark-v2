def sum_in_range(num_list):
    sum = 0
    for number in num_list:
        if number >= 5 and number <= 7:
            sum += number
    if sum == 0:
        return 0
    return sum