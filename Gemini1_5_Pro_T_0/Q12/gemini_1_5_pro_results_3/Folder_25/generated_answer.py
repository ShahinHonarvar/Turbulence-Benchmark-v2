def find_smallest_num(numbers):
    smallest = numbers[22]
    for i in range(22, 64):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest