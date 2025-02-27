def find_largest_num(numbers):
    largest = numbers[10]
    for i in range(10, 67):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest