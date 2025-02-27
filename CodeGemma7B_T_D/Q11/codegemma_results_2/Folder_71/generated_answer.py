def find_largest_num(numbers):
    largest = float('-inf')
    for i in range(26, 53):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest