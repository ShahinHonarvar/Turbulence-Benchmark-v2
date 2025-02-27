def find_second_largest_num(numbers):
    subset = numbers[26:55]
    if len(subset) < 2:
        return None
    max_num = max(subset)
    subset.remove(max_num)
    if len(subset) == 1:
        return None
    return max(subset)