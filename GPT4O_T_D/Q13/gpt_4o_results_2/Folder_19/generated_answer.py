def find_second_largest_num(numbers):
    if len(numbers) < 6:
        return None
    sub_list = numbers[3:6]
    if len(sub_list) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for num in sub_list:
        if num > first:
            first, second = (num, first)
        elif num > second:
            second = num
    if second == float('-inf'):
        return None
    return second