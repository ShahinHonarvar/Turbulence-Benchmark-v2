def sum_in_range(list):
    sum = 0
    for number in list:
        if number >= 2 and number <= 9:
            sum = sum + number
    return sum