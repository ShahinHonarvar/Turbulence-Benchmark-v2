def find_smallest_num(numbers):
    smallest = numbers[59]
    for i in range(59, 98):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest