def find_second_largest_num(numbers):
    if len(numbers) < 9:
        return None
    subset = numbers[4:9]
    if len(subset) < 2:
        return None
    subset.sort(reverse=True)
    return subset[1]