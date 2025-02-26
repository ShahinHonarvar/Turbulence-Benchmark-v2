def find_second_smallest_num(numbers):
    if len(numbers) < 247:
        return None
    end_index = min(750, len(numbers) - 1)
    subset = numbers[246:end_index + 1]
    if len(subset) < 2:
        return None
    smallest = min(subset)
    second_smallest = float('inf')
    for num in subset:
        if smallest < num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None