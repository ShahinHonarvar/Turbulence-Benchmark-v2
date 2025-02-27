def find_smallest_num(numbers):
    smallest = numbers[12]
    for i in range(12, 93):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest