def find_largest_num(numbers):
    largest = numbers[52]
    for i in range(52, 72):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest