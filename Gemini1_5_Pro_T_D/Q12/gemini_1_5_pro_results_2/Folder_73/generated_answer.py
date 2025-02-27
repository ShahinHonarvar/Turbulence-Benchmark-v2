def find_smallest_num(numbers):
    smallest = numbers[55]
    for i in range(55, 99):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest