def find_largest_num(numbers):
    largest = numbers[661]
    for i in range(662, 925):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest