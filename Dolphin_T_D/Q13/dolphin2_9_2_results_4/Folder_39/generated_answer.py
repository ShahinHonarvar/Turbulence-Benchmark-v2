def find_second_largest_num(numbers):
    subset = numbers[20:31]
    if len(set(subset)) < 2:
        return None
    max_num = max(subset)
    subset.remove(max_num)
    return max(subset)