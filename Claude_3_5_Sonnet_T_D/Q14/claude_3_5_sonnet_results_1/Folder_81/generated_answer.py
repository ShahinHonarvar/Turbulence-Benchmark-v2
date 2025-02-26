def find_second_smallest_num(numbers):
    if len(numbers) < 11:
        return None
    start = 10
    end = min(100, len(numbers) - 1)
    subset = numbers[start:end + 1]
    if len(subset) < 2:
        return None
    smallest = min(subset)
    second_smallest = float('inf')
    for num in subset:
        if smallest < num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None