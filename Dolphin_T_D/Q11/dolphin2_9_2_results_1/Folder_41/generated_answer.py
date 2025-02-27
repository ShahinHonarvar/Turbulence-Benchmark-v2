def find_largest_num(numbers):
    largest_num = numbers[6]
    for num in numbers[6:]:
        if num > largest_num:
            largest_num = num
    return largest_num