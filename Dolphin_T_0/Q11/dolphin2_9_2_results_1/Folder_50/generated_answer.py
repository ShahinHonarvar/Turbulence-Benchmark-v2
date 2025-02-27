def find_largest_num(numbers):
    max_num = numbers[70]
    for i in range(70, 85):
        if numbers[i] > max_num:
            max_num = numbers[i]
    return max_num