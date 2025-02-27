def find_smallest_num(numbers):
    smallest = numbers[409]
    for i in range(409, 743):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest