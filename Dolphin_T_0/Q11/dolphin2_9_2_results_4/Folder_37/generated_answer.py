def find_largest_num(numbers):
    max_num = numbers[1]
    for num in numbers[1:6]:
        if num > max_num:
            max_num = num
    return max_num