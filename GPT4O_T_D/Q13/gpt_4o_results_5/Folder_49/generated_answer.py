def find_second_largest_num(numbers):
    if len(numbers) < 201 or 80 > len(numbers) - 1:
        return None
    section = numbers[80:201]
    if len(section) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for num in section:
        if num > first:
            first, second = (num, first)
        elif num > second:
            second = num
    return second if second != float('-inf') else None