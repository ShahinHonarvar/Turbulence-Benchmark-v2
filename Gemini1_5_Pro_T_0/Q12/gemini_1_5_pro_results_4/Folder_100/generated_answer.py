def find_smallest_num(numbers):
    smallest = numbers[17]
    for i in range(17, 79):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest