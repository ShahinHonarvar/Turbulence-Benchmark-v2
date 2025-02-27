def find_largest_num(numbers):
    largest_num = numbers[10]
    for i in range(10, 67):
        if numbers[i] > largest_num:
            largest_num = numbers[i]
    return largest_num