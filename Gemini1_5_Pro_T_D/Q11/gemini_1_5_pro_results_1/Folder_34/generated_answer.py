def find_largest_num(numbers):
    largest = numbers[60]
    for i in range(60, 201):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest