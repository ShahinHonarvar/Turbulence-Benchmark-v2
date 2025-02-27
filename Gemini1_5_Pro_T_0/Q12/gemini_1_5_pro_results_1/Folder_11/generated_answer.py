def find_smallest_num(numbers):
    smallest = numbers[25]
    for i in range(25, 60):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest