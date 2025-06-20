def find_second_smallest_num(numbers):
    if len(numbers) < 69:
        return None
    sublist = numbers[42:69]
    if len(sublist) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for num in sublist:
        if num < first:
            first, second = (num, first)
        elif first < num < second:
            second = num
    return second if second != float('inf') else None