def find_smallest_num(numbers):
    smallest = float('inf')
    for num in numbers:
        if num < smallest and 0 <= num <= 9:
            smallest = num
    return smallest