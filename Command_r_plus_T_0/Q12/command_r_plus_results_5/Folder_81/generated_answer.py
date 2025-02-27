def find_smallest_num(numbers):
    smallest = float('inf')
    for i in range(10, 101):
        if i < len(numbers) and numbers[i] < smallest:
            smallest = numbers[i]
    return smallest