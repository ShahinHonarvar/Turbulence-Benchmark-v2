def find_largest_num(numbers):
    largest = numbers[1]
    for i in range(2, 6):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest