def find_largest_num(numbers):
    largest = numbers[20]
    for i in range(21, 31):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest