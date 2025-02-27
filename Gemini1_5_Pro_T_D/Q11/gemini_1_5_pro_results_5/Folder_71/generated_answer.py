def find_largest_num(numbers):
    largest = numbers[26]
    for i in range(27, 53):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest