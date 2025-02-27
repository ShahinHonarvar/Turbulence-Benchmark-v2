def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 9:
        return None
    sublist = numbers[:9]
    first, second = (float('-inf'), float('-inf'))
    for num in sublist:
        if num > first:
            first, second = (num, first)
        elif num > second:
            second = num
    return second if second != float('-inf') else None