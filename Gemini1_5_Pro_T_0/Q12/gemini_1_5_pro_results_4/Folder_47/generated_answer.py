def find_smallest_num(numbers):
    smallest = numbers[37]
    for i in range(37, 52):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest