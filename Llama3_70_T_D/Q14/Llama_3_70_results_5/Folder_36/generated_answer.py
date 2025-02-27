def find_second_smallest_num(numbers):
    if len(numbers) < 557:
        return None
    subset = numbers[209:557]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[1]