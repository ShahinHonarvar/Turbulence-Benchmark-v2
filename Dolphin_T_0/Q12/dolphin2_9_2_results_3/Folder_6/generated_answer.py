def find_smallest_num(numbers):
    smallest = float('inf')
    for num in numbers[21:98]:
        if num < smallest:
            smallest = num
    return smallest