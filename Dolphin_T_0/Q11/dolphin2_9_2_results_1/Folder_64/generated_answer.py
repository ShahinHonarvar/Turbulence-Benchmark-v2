def find_largest_num(numbers):
    max_num = numbers[0]
    for i in range(1, 5):
        if numbers[i] > max_num:
            max_num = numbers[i]
    return max_num