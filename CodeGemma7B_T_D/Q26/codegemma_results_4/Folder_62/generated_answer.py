def sum_in_range(list_of_numbers):
    sum = 0
    for number in list_of_numbers:
        if number >= -28 and number <= 573:
            sum += number
    return sum