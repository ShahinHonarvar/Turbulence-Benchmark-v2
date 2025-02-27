def find_largest_num(numbers):
    largest = float('-inf')
    for i in range(42, 69):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest