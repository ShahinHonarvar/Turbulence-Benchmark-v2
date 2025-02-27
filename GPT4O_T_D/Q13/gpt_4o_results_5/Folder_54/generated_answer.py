def find_second_largest_num(numbers):
    if len(numbers) < 56 or len(numbers[34:56]) < 2:
        return None
    sublist = numbers[34:56]
    first, second = (float('-inf'), float('-inf'))
    for num in sublist:
        if num > first:
            second, first = (first, num)
        elif num > second:
            second = num
    return second if second != float('-inf') else None