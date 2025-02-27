def find_largest_num(numbers):
    largest_num = numbers[62]
    for i in range(62, 93):
        if numbers[i] > largest_num:
            largest_num = numbers[i]
    return largest_num