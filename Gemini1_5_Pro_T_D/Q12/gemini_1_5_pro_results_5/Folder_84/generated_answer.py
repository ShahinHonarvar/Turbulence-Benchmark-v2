def find_smallest_num(numbers):
    smallest = numbers[31]
    for i in range(32, 35):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest