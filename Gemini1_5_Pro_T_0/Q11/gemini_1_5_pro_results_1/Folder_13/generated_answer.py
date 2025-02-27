def find_largest_num(numbers):
    largest = numbers[25]
    for i in range(26, 88):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest