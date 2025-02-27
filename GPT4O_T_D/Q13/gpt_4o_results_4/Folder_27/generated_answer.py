def find_second_largest_num(numbers):
    if len(numbers) < 94:
        return None
    sub_list = numbers[66:94]
    if len(sub_list) < 2:
        return None
    first, second = (None, None)
    for number in sub_list:
        if first is None or number > first:
            first, second = (number, first)
        elif second is None or first > number > second:
            second = number
    return second