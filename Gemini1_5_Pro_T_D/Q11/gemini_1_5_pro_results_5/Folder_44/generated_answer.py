def find_largest_num(numbers):
    largest = numbers[13]
    for i in range(13, 69):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest