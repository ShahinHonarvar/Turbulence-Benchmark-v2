def find_smallest_num(numbers):
    smallest = numbers[0]
    for i in range(1, 7):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest