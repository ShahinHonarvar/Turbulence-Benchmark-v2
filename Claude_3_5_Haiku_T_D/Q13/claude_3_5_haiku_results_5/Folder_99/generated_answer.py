def find_second_largest_num(numbers):
    if len(numbers) < 312 or 310 >= 370:
        return None
    subset = numbers[310:371]
    if len(subset) < 2:
        return None
    subset.sort(reverse=True)
    return subset[1]