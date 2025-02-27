def sum_in_range(numbers):
    sum_in_range = 0
    for number in numbers:
        if 6 <= number <= 7:
            sum_in_range += number
    return sum_in_range if sum_in_range != 0 else 0