def find_second_largest_num(numbers):
    values = numbers[639:976]
    if len(values) < 2:
        return None
    largest = max(values)
    second_largest = None
    for num in values:
        if num != largest and (second_largest is None or num > second_largest):
            second_largest = num
    return second_largest