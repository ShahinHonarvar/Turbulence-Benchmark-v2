def find_second_smallest_num(numbers):
    if len(numbers) < 202:
        return None
    subset = numbers[80:201]
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