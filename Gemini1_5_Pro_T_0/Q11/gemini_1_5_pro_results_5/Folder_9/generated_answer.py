def find_largest_num(numbers):
    largest = numbers[70]
    for i in range(70, 201):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest