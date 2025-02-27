def find_smallest_num(numbers):
    smallest = numbers[66]
    for i in range(66, 78):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest