def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    segment = numbers[:6]
    if len(segment) < 2:
        return None
    smallest = float('inf')
    second_smallest = float('inf')
    for num in segment:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None