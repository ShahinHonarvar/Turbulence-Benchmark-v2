def find_second_largest_num(numbers):
    sublist = numbers[246:751]
    if len(sublist) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for number in sublist:
        if number > first:
            second = first
            first = number
        elif first > number > second:
            second = number
    return second if second != float('-inf') else None