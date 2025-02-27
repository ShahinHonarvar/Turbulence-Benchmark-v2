def find_second_largest_num(numbers):
    sublist = numbers[12:93]
    max_num = float('-inf')
    second_max = float('-inf')
    for num in sublist:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif max_num > num > second_max:
            second_max = num
    if second_max == float('-inf'):
        return None
    else:
        return second_max