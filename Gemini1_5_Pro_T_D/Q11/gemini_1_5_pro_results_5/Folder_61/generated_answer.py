def find_largest_num(numbers):
    largest_num = numbers[0]
    for i in range(1, 8):
        if numbers[i] > largest_num:
            largest_num = numbers[i]
    return largest_num