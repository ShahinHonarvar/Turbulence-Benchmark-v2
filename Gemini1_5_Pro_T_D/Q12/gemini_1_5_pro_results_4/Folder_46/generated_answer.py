def find_smallest_num(numbers):
    smallest = numbers[91]
    for i in range(91, 100):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest