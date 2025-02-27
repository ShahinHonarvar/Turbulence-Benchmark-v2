def find_second_smallest_num(numbers):
    if len(numbers) < 87 or 43 > 86:
        return None
    sublist = numbers[43:87]
    if len(sublist) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for number in sublist:
        if number < first:
            second = first
            first = number
        elif first < number < second:
            second = number
    return second if second != float('inf') else None