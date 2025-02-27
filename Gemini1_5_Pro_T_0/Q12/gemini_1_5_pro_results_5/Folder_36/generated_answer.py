def find_smallest_num(numbers):
    smallest = numbers[310]
    for i in range(311, 371):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest