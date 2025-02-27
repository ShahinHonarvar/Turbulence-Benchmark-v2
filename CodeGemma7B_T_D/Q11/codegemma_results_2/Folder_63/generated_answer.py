def find_largest_num(numbers):
    largest = float('-inf')
    for i in range(22, 89):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest