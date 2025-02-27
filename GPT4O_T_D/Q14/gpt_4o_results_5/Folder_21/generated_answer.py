def find_second_smallest_num(numbers):
    if len(numbers) < 925:
        return None
    sublist = numbers[661:925]
    if len(sublist) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for num in sublist:
        if num < first:
            second = first
            first = num
        elif num < second:
            second = num
    return second if second != float('inf') else None