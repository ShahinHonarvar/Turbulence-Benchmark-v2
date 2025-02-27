def find_smallest_num(numbers):
    smallest = numbers[10]
    for i in range(10, 101):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest