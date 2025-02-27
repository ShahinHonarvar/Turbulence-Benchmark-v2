def find_smallest_num(numbers):
    smallest = float('inf')
    for num in numbers:
        if num >= 60 and num <= 200:
            if num < smallest:
                smallest = num
    return smallest