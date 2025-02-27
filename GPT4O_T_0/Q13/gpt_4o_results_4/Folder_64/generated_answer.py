def find_second_largest_num(numbers):
    if len(numbers) < 5:
        return None
    sub_list = numbers[:5]
    first, second = (float('-inf'), float('-inf'))
    for num in sub_list:
        if num > first:
            first, second = (num, first)
        elif num > second:
            second = num
    return second if second != float('-inf') else None