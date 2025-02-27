def find_smallest_num(numbers):
    smallest = float('inf')
    for num in numbers[32:36]:
        if num < smallest:
            smallest = num
    return smallest