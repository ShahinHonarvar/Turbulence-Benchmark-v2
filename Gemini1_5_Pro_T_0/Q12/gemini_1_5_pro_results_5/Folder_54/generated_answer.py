def find_smallest_num(numbers):
    smallest = numbers[74]
    for i in range(74, 96):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest