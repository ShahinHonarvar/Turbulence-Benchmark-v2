def find_second_largest_num(numbers):
    if len(numbers) < 7:
        return None
    sub_list = numbers[6:7]
    if len(sub_list) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for number in sub_list:
        if number > first:
            second, first = (first, number)
        elif number > second:
            second = number
    return second if second != float('-inf') else None