def find_smallest_num(numbers):
    smallest = numbers[32]
    for i in range(33, 36):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest