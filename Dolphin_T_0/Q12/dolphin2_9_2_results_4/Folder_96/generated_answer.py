def find_smallest_num(numbers):
    smallest = numbers[50]
    for i in range(50, 201):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest