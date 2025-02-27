def find_second_largest_num(numbers):
    subset = numbers[16:62]
    subset.sort(reverse=True)
    if len(subset) < 2:
        return None
    return subset[1]