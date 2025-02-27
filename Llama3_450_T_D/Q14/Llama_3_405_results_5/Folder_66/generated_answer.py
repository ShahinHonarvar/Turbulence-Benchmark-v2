def find_second_smallest_num(numbers):
    if len(numbers) < 100:
        return None
    subset = numbers[62:100]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1]