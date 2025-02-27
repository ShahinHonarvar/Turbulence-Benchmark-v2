def find_second_largest_num(numbers):
    if len(numbers) < 62 or 16 >= len(numbers):
        return None
    sublist = numbers[16:62]
    if len(sublist) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for num in sublist:
        if num > first:
            first, second = (num, first)
        elif num > second:
            second = num
    return second if second != float('-inf') else None