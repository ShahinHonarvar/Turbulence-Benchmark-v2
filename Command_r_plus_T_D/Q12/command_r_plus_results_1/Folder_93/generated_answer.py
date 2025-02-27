def find_smallest_num(numbers):
    smallest = float('inf')
    for i in range(29, 94):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest