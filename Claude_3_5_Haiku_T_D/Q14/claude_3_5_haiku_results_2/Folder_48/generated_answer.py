def find_second_smallest_num(numbers):
    if len(numbers) < 248:
        return None
    subset = numbers[246:751]
    if len(subset) < 2:
        return None
    try:
        smallest = min(subset)
        subset_without_smallest = [num for num in subset if num != smallest]
        if not subset_without_smallest:
            return None
        return min(subset_without_smallest)
    except ValueError:
        return None