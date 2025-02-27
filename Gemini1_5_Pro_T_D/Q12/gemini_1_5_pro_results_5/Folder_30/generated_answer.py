def find_smallest_num(numbers):
    smallest = numbers[29]
    for i in range(29, 52):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest