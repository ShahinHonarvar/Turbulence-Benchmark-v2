def find_largest_num(numbers):
    largest = numbers[35]
    for i in range(35, 50):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest