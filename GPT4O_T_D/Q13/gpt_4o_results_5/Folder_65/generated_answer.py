def find_second_largest_num(numbers):
    if len(numbers) < 99 or 56 > 98:
        return None
    segment = numbers[56:99]
    if len(segment) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for num in segment:
        if num > first:
            second, first = (first, num)
        elif num > second and num != first:
            second = num
    return second if second != float('-inf') else None