def find_second_largest_num(numbers):
    sub_list = numbers[75:86]
    if len(sub_list) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for number in sub_list:
        if number > first:
            first, second = (number, first)
        elif number > second:
            second = number
    return second if second != float('-inf') else None