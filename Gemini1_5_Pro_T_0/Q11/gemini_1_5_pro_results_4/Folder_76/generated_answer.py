def find_largest_num(numbers):
    largest = numbers[686]
    for i in range(687, 988):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest