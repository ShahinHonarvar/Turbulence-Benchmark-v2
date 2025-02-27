def find_smallest_num(numbers):
    smallest = numbers[22]
    for i in range(22, 51):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest