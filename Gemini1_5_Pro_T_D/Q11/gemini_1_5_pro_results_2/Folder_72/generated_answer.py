def find_largest_num(numbers):
    largest = numbers[29]
    for i in range(29, 52):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest