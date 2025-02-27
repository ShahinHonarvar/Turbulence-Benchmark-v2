def find_largest_num(numbers):
    largest = numbers[15]
    for i in range(15, 40):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest