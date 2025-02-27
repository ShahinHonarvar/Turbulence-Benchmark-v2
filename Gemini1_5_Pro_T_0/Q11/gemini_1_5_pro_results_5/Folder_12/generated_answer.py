def find_largest_num(numbers):
    largest = numbers[14]
    for i in range(14, 65):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest