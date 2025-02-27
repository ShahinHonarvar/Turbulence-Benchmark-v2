def find_largest_num(numbers):
    largest = numbers[28]
    for i in range(29, 39):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest