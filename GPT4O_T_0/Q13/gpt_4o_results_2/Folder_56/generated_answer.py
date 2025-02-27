def find_second_largest_num(numbers):
    if len(numbers) <= 1:
        return None
    first, second = (float('-inf'), float('-inf'))
    for num in numbers:
        if num > first:
            second = first
            first = num
        elif num > second:
            second = num
    return second if second != float('-inf') else None