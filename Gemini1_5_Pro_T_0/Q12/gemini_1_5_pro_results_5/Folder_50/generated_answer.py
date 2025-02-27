def find_smallest_num(numbers):
    smallest = numbers[43]
    for i in range(43, 52):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest