def find_second_smallest_num(numbers):
    if not numbers or len(numbers) <= 71:
        return None
    subset = numbers[70:201]
    if len(subset) < 2:
        return None
    first_smallest = float('inf')
    second_smallest = float('inf')
    for num in subset:
        if num < first_smallest:
            second_smallest = first_smallest
            first_smallest = num
        elif num < second_smallest and num != first_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None