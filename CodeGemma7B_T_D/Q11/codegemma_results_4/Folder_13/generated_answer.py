def find_largest_num(numbers):
    largest_num = float('-inf')
    for num in numbers[25:88]:
        if num > largest_num:
            largest_num = num
    return largest_num