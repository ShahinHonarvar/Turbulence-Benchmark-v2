def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    subset = numbers[0:4]
    if len(subset) < 2:
        return None
    smallest = min(subset)
    second_smallest = None
    for num in subset:
        if num != smallest and (second_smallest is None or num < second_smallest):
            second_smallest = num
    return second_smallest