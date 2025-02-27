def find_second_largest_num(numbers):
    sublist = numbers[66:94]
    if len(sublist) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for num in sublist:
        if num > first:
            first, second = (num, first)
        elif num > second and num != first:
            second = num
    return second if second != float('-inf') else None