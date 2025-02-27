def find_second_largest_num(numbers):
    if len(numbers) < 93:
        return None
    selected_numbers = numbers[19:93]
    if len(selected_numbers) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for number in selected_numbers:
        if number > first:
            first, second = (number, first)
        elif first > number > second:
            second = number
    return second if second != float('-inf') else None