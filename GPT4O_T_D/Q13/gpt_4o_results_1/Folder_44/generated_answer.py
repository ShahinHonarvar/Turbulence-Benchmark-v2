def find_second_largest_num(numbers):
    if len(numbers) < 69:
        return None
    sublist = numbers[13:69]
    if len(sublist) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for num in sublist:
        if num > first:
            first, second = (num, first)
        elif first > num > second:
            second = num
    return None if second == float('-inf') else second