def find_second_largest_num(numbers):
    if len(numbers) < 52 or len(set(numbers[15:52])) < 2:
        return None
    sub_list = numbers[15:52]
    first, second = (float('-inf'), float('-inf'))
    for num in sub_list:
        if num > first:
            first, second = (num, first)
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None