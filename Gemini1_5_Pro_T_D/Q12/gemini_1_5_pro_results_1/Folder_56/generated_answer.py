def find_smallest_num(numbers):
    smallest = numbers[1]
    for i in range(2, 9):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest