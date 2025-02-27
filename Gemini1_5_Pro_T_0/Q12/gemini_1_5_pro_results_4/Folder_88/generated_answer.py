def find_smallest_num(numbers):
    smallest = numbers[6]
    for i in range(6, 9):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest