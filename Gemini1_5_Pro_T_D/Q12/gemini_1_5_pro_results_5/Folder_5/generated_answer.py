def find_smallest_num(numbers):
    smallest = numbers[3]
    for i in range(3, 6):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest