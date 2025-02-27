def find_smallest_num(numbers):
    smallest = numbers[60]
    for i in range(60, 201):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest