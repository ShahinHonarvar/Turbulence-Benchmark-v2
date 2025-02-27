def find_second_largest_num(numbers):
    if len(numbers) < 88:
        return None
    sublist = numbers[30:88]
    if len(sublist) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for num in sublist:
        if num > first:
            first, second = (num, first)
        elif num > second:
            second = num
    return second if second != float('-inf') else None