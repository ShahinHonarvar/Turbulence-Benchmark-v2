def find_smallest_num(numbers):
    smallest = numbers[70]
    for i in range(71, 201):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest