def find_largest_num(numbers):
    max_num = float('-inf')
    for num in numbers[35:50]:
        if num > max_num:
            max_num = num
    return max_num