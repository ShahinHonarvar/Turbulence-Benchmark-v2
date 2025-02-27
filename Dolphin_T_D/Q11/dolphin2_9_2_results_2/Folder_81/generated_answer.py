def find_largest_num(numbers):
    max_num = float('-inf')
    for num in numbers[10:101]:
        if num > max_num:
            max_num = num
    return max_num