def find_largest_num(numbers):
    largest = float('-inf')
    for i in range(4, 9):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest