def find_largest_num(numbers):
    largest = numbers[82]
    for i in range(83, 87):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest