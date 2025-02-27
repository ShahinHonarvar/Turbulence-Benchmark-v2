def find_smallest_num(numbers):
    smallest = numbers[30]
    for i in range(30, 49):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest