def find_smallest_num(numbers):
    min_num = float('inf')
    for i in range(6, 7):
        if numbers[i] < min_num:
            min_num = numbers[i]
    return min_num