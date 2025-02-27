def sum_in_range(lst):
    sum = 0
    for number in lst:
        if number in range(6, 9):
            sum += number
    return sum