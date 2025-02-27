def find_largest_num(numbers):
    largest = numbers[310]
    for i in range(311, 371):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest