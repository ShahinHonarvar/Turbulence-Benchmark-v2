def find_largest_num(numbers):
    max_num = None
    for num in numbers[40:81]:
        if max_num is None or num > max_num:
            max_num = num
    return max_num