def find_second_largest_num(numbers):
    if len(numbers) < 371:
        return None
    subset = numbers[310:371]
    subset.sort(reverse=True)
    if len(subset) < 2:
        return None
    return subset[1]