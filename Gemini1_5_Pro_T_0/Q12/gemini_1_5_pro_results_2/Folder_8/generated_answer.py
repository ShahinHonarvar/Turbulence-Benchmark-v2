def find_smallest_num(numbers):
    smallest = numbers[75]
    for i in range(75, 95):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest