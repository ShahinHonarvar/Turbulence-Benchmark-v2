def find_largest_num(numbers):
    largest = numbers[639]
    for i in range(639, 976):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest