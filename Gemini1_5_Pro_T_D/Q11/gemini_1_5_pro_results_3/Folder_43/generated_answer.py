def find_largest_num(numbers):
    largest_num = numbers[68]
    for i in range(68, 87):
        if numbers[i] > largest_num:
            largest_num = numbers[i]
    return largest_num