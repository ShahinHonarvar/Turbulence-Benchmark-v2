def find_second_largest_num(numbers):
    filtered_numbers = numbers[56:67]
    if len(filtered_numbers) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for number in filtered_numbers:
        if number > first:
            first, second = (number, first)
        elif first > number > second:
            second = number
    return second if second != float('-inf') else None