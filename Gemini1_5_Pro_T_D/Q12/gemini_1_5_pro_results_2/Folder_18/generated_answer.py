def find_smallest_num(numbers):
    smallest = numbers[15]
    for i in range(16, 40):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest