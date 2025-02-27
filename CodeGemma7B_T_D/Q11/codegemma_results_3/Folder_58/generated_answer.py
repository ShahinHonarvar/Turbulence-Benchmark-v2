def find_largest_num(numbers):
    largest = float('-inf')
    for i in range(209, 557):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest