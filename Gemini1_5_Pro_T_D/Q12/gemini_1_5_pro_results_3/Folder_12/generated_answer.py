def find_smallest_num(numbers):
    smallest = numbers[34]
    for i in range(34, 56):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest