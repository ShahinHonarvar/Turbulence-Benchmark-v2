def find_largest_num(numbers):
    largest = numbers[37]
    for i in range(37, 77):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest