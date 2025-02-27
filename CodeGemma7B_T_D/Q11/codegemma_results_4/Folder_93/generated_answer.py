def find_largest_num(numbers):
    largest_num = float('-inf')
    for i in range(75, 95):
        if numbers[i] > largest_num:
            largest_num = numbers[i]
    return largest_num