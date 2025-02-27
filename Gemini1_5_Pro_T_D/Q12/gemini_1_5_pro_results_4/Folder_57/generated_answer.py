def find_smallest_num(numbers):
    smallest = numbers[28]
    for i in range(29, 41):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest