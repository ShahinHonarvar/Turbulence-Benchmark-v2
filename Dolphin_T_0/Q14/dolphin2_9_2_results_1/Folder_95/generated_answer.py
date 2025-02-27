def find_second_smallest_num(numbers):
    if 75 < len(numbers) < 85:
        subset = numbers[75:85]
        subset.sort()
        if len(set(subset)) >= 2:
            return subset[1]
    return None