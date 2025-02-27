def find_smallest_num(numbers):
    smallest = numbers[70]
    for i in range(70, 201):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest