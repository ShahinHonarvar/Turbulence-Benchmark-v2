def find_second_largest_num(numbers):
    if len(numbers) < 87 or len(numbers[75:86]) < 2:
        return None
    subset = numbers[75:86]
    sorted_subset = sorted(subset, reverse=True)
    return sorted_subset[1]