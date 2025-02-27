def find_second_largest_num(numbers):
    sub_list = numbers[50:55]
    if len(sub_list) < 2:
        return None
    first, second = (None, None)
    for num in sub_list:
        if first is None or num > first:
            second = first
            first = num
        elif second is None or num > second:
            second = num
    return second