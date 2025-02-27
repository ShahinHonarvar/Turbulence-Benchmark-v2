def find_largest_num(numbers):
    largest_num = numbers[0]
    for num in numbers[1:]:
        if num > largest_num:
            largest_num = num
    return largest_num