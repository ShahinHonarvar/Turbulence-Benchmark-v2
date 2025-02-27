def find_second_largest_num(numbers):
    if len(numbers) < 72:
        return None
    sub_list = numbers[52:72]
    if len(sub_list) < 2:
        return None
    first, second = (None, None)
    for num in sub_list:
        if first is None or num > first:
            first, second = (num, first)
        elif second is None or first > num > second:
            second = num
    return second