def find_smallest_num(numbers):
    smallest = numbers[21]
    for i in range(21, 98):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest