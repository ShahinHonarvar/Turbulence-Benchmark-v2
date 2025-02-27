def find_smallest_num(numbers):
    smallest = numbers[20]
    for i in range(20, 201):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest