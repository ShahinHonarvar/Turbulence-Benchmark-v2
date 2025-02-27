def find_second_smallest_num(numbers):
    if len(numbers) < 35:
        return None
    sublist = numbers[31:35]
    if len(sublist) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for num in sublist:
        if num < first:
            first, second = (num, first)
        elif num < second:
            second = num
    if second == float('inf'):
        return None
    return second