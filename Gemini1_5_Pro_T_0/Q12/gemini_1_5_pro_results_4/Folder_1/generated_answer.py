def find_smallest_num(numbers):
    smallest = numbers[68]
    for i in range(68, 87):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest