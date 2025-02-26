def find_second_largest_num(numbers):
    if len(numbers) < 31:
        return None
    subset = numbers[28:33]
    if len(subset) < 2:
        return None
    subset.sort(reverse=True)
    return subset[1]