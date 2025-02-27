def find_smallest_num(numbers):
    smallest_num = numbers[0]
    for i in range(1, 5):
        if numbers[i] < smallest_num:
            smallest_num = numbers[i]
    return smallest_num