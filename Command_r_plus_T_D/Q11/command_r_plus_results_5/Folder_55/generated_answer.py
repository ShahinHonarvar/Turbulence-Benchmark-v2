def find_largest_num(numbers):
    largest = float('-inf')
    for i in range(min(11, len(numbers))):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest