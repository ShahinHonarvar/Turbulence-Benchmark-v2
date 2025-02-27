def find_second_largest_num(numbers):
    if len(numbers[246:751]) < 2:
        return None
    max_num = second_max = float('-inf')
    for num in numbers[246:751]:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif num > second_max and num < max_num:
            second_max = num
    return second_max