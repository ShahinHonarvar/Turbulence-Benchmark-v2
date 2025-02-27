def sum_in_range(integers):
    sum_of_integers = 0
    for number in integers:
        if number >= 4 and number <= 8:
            sum_of_integers += number
    return sum_of_integers