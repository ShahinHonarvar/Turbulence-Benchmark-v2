def find_smallest_num(numbers):
    smallest = numbers[36]
    for i in range(37, 47):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest