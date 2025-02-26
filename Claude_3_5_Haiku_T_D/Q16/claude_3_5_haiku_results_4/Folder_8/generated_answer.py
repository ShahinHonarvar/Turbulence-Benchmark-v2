def sum_even_ints_inclusive(numbers):
    if len(numbers) <= 23:
        return 0
    number_at_23 = numbers[23]
    if number_at_23 % 2 == 0:
        return number_at_23
    else:
        return 0