def find_second_largest_num(numbers):
    sub_list = numbers[28:39]
    if len(sub_list) < 2:
        return None
    first = second = float('-inf')
    for num in sub_list:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None