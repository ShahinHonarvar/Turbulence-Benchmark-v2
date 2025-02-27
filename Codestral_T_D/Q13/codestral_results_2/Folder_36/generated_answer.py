def find_second_largest_num(numbers):
    sublist = numbers[246:751]
    if len(sublist) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for num in sublist:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    if second == float('-inf'):
        return None
    return second