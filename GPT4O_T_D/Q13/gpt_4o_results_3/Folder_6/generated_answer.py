def find_second_largest_num(numbers):
    if len(numbers) < 67:
        return None
    sub_list = numbers[10:67]
    if len(sub_list) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for num in sub_list:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second if second != float('-inf') else None