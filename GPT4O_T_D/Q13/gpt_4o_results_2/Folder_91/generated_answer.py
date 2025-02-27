def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers[0:6]) < 2:
        return None
    sub_list = numbers[0:6]
    first, second = (float('-inf'), float('-inf'))
    for number in sub_list:
        if number > first:
            second = first
            first = number
        elif number > second:
            second = number
    return second if second != float('-inf') else None