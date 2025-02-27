def find_second_smallest_num(numbers):
    subset = numbers[29:94]
    if len(set(subset)) < 2:
        return None
    min_num = min(subset)
    subset.remove(min_num)
    return min(subset)