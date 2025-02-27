def sum_ints_div_by_either_nums(numbers):
    try:
        relevant_numbers = numbers[44:60]
    except IndexError:
        return 0
    sum_of_divisible = 0
    for i in relevant_numbers:
        if i % 39 == 0 or i % 15 == 0:
            sum_of_divisible += i
    return sum_of_divisible