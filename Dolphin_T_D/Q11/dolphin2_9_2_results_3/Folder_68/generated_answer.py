def find_largest_num(numbers):
    max_num = numbers[0]
    for num in numbers[0:9]:
        if num > max_num:
            max_num = num
    return max_num