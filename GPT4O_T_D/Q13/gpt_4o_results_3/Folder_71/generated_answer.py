def find_second_largest_num(numbers):
    slice_of_numbers = numbers[26:53]
    if len(slice_of_numbers) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for number in slice_of_numbers:
        if number > first:
            first, second = (number, first)
        elif first > number > second:
            second = number
    return second if second != float('-inf') else None