def find_second_smallest_num(numbers):
    if len(numbers) < 64:
        return None
    subset = numbers[22:64]
    if len(subset) < 2:
        return None
    smallest = min(subset)
    second_smallest = float('inf')
    for num in subset:
        if smallest < num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None