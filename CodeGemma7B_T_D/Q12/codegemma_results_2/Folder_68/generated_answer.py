def find_smallest_num(numbers):
    smallest_num = float('inf')
    for i in range(0, 8):
        if numbers[i] < smallest_num:
            smallest_num = numbers[i]
    return smallest_num