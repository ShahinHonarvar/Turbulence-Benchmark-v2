def find_second_largest_num(numbers):
    if len(numbers) < 6:
        return None
    sub_list = numbers[:6]
    first, second = (float('-inf'), float('-inf'))
    for number in sub_list:
        if number > first:
            second, first = (first, number)
        elif number > second:
            second = number
    return second if second != float('-inf') else None