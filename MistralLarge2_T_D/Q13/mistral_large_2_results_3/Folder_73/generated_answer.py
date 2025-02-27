def find_second_largest_num(numbers):
    if len(numbers) < 93:
        return None
    subset = numbers[19:93]
    if len(subset) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for num in subset:
        if num > first:
            first, second = (num, first)
        elif num > second and num != first:
            second = num
    return second if second != float('-inf') else None