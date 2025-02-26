def find_second_smallest_num(numbers):
    if len(numbers) <= 12 or len(numbers) <= 92:
        return None
    subset = numbers[12:93]
    if len(subset) < 2:
        return None
    smallest = float('inf')
    second_smallest = float('inf')
    for num in subset:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None