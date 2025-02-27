def find_second_largest_num(numbers):
    subrange = numbers[36:47]
    if len(subrange) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for number in subrange:
        if number > first:
            first, second = (number, first)
        elif first > number > second:
            second = number
    return second if second != float('-inf') else None