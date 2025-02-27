def find_smallest_num(numbers):
    smallest = numbers[209]
    for i in range(210, 557):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest