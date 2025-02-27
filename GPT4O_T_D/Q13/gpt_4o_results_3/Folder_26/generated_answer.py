def find_second_largest_num(numbers):
    if len(numbers) < 100:
        return None
    sub_list = numbers[62:100]
    if len(sub_list) < 2:
        return None
    first, second = (None, None)
    for num in sub_list:
        if first is None or num > first:
            first, second = (num, first)
        elif second is None or (num > second and num != first):
            second = num
    return second