def find_largest_num(numbers):
    largest = numbers[533]
    for i in range(533, 606):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest