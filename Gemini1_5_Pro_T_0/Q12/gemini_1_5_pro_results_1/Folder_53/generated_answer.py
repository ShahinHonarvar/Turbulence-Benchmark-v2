def find_smallest_num(numbers):
    smallest = numbers[100]
    for i in range(101, 201):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest