def find_smallest_num(numbers):
    smallest = numbers[2]
    for i in range(3, 7):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest