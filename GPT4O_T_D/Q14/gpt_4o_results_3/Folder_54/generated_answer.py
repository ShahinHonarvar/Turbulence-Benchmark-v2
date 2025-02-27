def find_second_smallest_num(numbers):
    if len(numbers) < 87 or 68 > 86:
        return None
    sublist = numbers[68:87]
    if len(sublist) < 2:
        return None
    first_min, second_min = (float('inf'), float('inf'))
    for number in sublist:
        if number < first_min:
            first_min, second_min = (number, first_min)
        elif first_min < number < second_min:
            second_min = number
    return second_min if second_min != float('inf') else None