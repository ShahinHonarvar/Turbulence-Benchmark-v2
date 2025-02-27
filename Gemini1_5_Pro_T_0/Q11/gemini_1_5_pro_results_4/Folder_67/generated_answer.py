def find_largest_num(numbers):
    largest = numbers[22]
    for i in range(22, 51):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest