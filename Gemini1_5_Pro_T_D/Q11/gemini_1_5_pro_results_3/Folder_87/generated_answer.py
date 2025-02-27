def find_largest_num(numbers):
    largest = numbers[36]
    for i in range(37, 47):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest