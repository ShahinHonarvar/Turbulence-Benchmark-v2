def find_second_smallest_num(numbers):
    subset = numbers[29:94]
    if len(subset) < 2:
        return None
    smallest = float('inf')
    second_smallest = float('inf')
    for num in subset:
        if num <= smallest:
            smallest, second_smallest = (num, smallest)
        elif num < second_smallest:
            second_smallest = num
    if second_smallest == float('inf'):
        return None
    return second_smallest