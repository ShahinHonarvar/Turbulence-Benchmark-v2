def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    subset = numbers[:8]
    if len(subset) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for num in subset:
        if num < first:
            second = first
            first = num
        elif num < second:
            second = num
    return second if second != float('inf') else None