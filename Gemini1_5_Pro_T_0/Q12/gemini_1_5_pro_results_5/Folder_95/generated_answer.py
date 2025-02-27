def find_smallest_num(numbers):
    smallest = numbers[56]
    for i in range(56, 99):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest