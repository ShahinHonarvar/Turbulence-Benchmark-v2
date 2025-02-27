def find_second_largest_num(numbers):
    if len(numbers) < 55:
        return None
    sub_list = numbers[50:55]
    if len(sub_list) < 2:
        return None
    first, second = (None, None)
    for number in sub_list:
        if first is None or number > first:
            second = first
            first = number
        elif second is None or (number < first and number > second):
            second = number
    return second