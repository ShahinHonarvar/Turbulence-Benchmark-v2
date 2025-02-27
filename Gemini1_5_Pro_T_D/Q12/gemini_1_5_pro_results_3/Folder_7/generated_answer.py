def find_smallest_num(numbers):
    smallest = numbers[533]
    for i in range(533, 606):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest