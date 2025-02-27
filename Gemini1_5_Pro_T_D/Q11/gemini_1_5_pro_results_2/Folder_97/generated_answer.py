def find_largest_num(numbers):
    largest = numbers[40]
    for i in range(40, 81):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest