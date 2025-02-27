def find_second_largest_num(numbers):
    if len(numbers) < 2 or 246 > 750:
        return None
    sub_list = numbers[246:751]
    if len(sub_list) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for number in sub_list:
        if number > first:
            first, second = (number, first)
        elif first > number > second:
            second = number
    if second == float('-inf'):
        return None
    return second