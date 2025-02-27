def find_largest_num(numbers):
    largest = numbers[74]
    for i in range(74, 96):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest