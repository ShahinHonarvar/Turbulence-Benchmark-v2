def find_largest_num(numbers):
    largest_num = numbers[28]
    for num in numbers[29:33]:
        largest_num = max(num, largest_num)
    return largest_num