def find_largest_num(numbers):
    largest = numbers[34]
    for i in range(34, 56):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest