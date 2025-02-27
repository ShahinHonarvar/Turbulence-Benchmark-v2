def find_second_largest_num(numbers):
    sublist = numbers[42:69]
    if len(sublist) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for num in sublist:
        if num > first:
            first, second = (num, first)
        elif num > second:
            second = num
    if second == float('-inf'):
        return None
    return second