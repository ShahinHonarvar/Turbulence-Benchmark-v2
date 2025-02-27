def find_smallest_num(numbers):
    smallest = numbers[40]
    for i in range(40, 201):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest