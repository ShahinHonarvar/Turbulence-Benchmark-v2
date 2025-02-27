def find_second_largest_num(numbers):
    if len(numbers) <= 6:
        return None
    sub_array = numbers[6:7]
    if len(sub_array) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for num in sub_array:
        if num > first:
            first, second = (num, first)
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None