def find_largest_num(numbers):
    largest = numbers[246]
    for i in range(246, 751):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest