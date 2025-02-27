def find_smallest_num(numbers):
    smallest = numbers[27]
    for i in range(27, 56):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest