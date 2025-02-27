def find_smallest_num(numbers):
    smallest = numbers[19]
    for i in range(20, 93):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest