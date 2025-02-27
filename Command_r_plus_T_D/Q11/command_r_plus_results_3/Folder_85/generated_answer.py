def find_largest_num(numbers):
    largest = float('-inf')
    for i in range(6, 9):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest