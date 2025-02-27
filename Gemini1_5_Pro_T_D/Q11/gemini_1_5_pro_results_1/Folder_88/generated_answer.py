def find_largest_num(numbers):
    largest = numbers[4]
    for i in range(5, 9):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest