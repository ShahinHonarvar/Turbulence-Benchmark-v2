def find_largest_num(numbers):
    max_num = numbers[12]
    for num in numbers[12:92 + 1]:
        if num > max_num:
            max_num = num
    return max_num