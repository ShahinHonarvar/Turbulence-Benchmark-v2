def find_smallest_num(numbers):
    smallest = numbers[4]
    for i in range(5, 9):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest