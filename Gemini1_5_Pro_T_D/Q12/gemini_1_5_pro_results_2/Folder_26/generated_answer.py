def find_smallest_num(numbers):
    smallest = numbers[28]
    for i in range(28, 39):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest