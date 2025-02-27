def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    first = max(numbers[0], numbers[1])
    second = min(numbers[0], numbers[1])
    for i in numbers[2:]:
        if i > first:
            second = first
            first = i
        elif i > second:
            second = i
    if second == numbers[0:10][0]:
        return None
    return second