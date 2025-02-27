def find_smallest_num(numbers):
    if len(numbers) < 21:
        return None
    subset = numbers[20:201]
    return min(subset)