def find_second_smallest_num(numbers):
    if len(numbers) < 201:
        return None
    subrange = numbers[40:201]
    if len(subrange) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for number in subrange:
        if number < first:
            first, second = (number, first)
        elif first < number < second:
            second = number
    if second == float('inf'):
        return None
    return second