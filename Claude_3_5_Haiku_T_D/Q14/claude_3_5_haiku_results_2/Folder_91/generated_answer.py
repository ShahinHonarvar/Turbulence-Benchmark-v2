def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    subset = numbers[:6]
    if len(subset) < 2:
        return None
    first_smallest = min(subset)
    second_smallest = float('inf')
    for num in subset:
        if num < second_smallest and num != first_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None