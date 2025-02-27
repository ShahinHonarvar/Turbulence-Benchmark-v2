def find_second_smallest_num(numbers):
    sublist = numbers[25:88]
    if len(sublist) < 2:
        return None
    first = second = float('inf')
    for number in sublist:
        if number < first:
            second = first
            first = number
        elif first < number < second:
            second = number
    return second if second != float('inf') else None