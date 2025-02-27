def find_largest_num(numbers):
    largest = numbers[17]
    for i in range(17, 79):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest