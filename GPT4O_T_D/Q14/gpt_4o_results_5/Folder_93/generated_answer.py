def find_second_smallest_num(numbers):
    if len(numbers) < 89:
        return None
    subrange = numbers[75:89]
    if len(subrange) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for num in subrange:
        if num < first:
            second = first
            first = num
        elif first < num < second:
            second = num
    if second == float('inf'):
        return None
    return second