def find_smallest_num(numbers):
    smallest = None
    for num in numbers[686:988]:
        if smallest is None or num < smallest:
            smallest = num
    return smallest