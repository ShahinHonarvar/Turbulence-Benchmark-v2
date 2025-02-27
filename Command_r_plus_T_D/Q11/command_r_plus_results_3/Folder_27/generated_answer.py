def find_largest_num(numbers):
    largest = float('-inf')
    for i in range(66, 94):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest