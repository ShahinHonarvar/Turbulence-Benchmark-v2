def find_largest_num(numbers):
    largest = numbers[12]
    for i in range(12, 93):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest