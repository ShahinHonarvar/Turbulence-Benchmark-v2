def find_largest_num(numbers):
    largest = numbers[68]
    for i in range(68, 87):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest