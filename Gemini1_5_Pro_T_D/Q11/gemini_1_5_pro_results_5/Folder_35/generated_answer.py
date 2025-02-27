def find_largest_num(numbers):
    largest = numbers[30]
    for i in range(30, 49):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest