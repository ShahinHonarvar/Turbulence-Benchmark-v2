def find_second_smallest_num(numbers):
    if len(numbers) < 9:
        return None
    segment = numbers[4:9]
    if len(segment) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for number in segment:
        if number < first:
            first, second = (number, first)
        elif first < number < second:
            second = number
    return second if second != float('inf') else None