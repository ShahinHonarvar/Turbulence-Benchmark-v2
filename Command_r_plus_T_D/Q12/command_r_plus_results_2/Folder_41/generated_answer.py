def find_smallest_num(numbers):
    smallest = float('inf')
    for i in range(4, len(numbers)):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest