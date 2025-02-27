def find_smallest_num(numbers):
    smallest = numbers[35]
    for i in range(35, 50):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest