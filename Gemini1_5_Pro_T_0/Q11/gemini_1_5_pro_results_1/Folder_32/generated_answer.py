def find_largest_num(numbers):
    largest = numbers[21]
    for i in range(22, 98):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest