def find_second_smallest_num(numbers):
    slice_section = numbers[74:96]
    if len(slice_section) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for number in slice_section:
        if number < first:
            first, second = (number, first)
        elif first < number < second:
            second = number
    return second if second < float('inf') else None