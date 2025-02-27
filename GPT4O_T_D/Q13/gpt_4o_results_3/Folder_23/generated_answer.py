def find_second_largest_num(numbers):
    if len(numbers) < 72:
        return None
    sub_list = numbers[52:72]
    if len(sub_list) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for num in sub_list:
        if num > first:
            first, second = (num, first)
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None