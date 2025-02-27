def sum_in_range(list_of_integers):
    sum_of_numbers = 0
    for number in list_of_integers:
        if 5 <= number <= 9:
            sum_of_numbers += number
    return sum_of_numbers