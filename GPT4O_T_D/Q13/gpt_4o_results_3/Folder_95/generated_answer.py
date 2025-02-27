def find_second_largest_num(numbers):
    if len(numbers) < 87:
        return None
    sub_list = numbers[82:87]
    if len(set(sub_list)) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for num in sub_list:
        if num > first:
            second = first
            first = num
        elif num > second:
            second = num
    return second