def find_second_smallest_num(numbers):
    subset = numbers[27:56]
    if len(subset) < 2:
        return None
    else:
        subset.sort()
        return subset[1]