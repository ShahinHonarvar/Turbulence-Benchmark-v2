def find_largest_num(numbers):
    largest = numbers[21]
    for i in range(21, 98):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest