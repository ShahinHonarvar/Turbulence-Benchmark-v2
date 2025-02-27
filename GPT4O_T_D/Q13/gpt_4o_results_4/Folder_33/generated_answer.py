def find_second_largest_num(numbers):
    if len(numbers) < 775 or len(set(numbers[667:775])) < 2:
        return None
    segment = numbers[667:775]
    first, second = (float('-inf'), float('-inf'))
    for number in segment:
        if number > first:
            first, second = (number, first)
        elif first > number > second:
            second = number
    return second if second != float('-inf') else None