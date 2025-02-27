def find_second_smallest_num(numbers):
    subset = numbers[17:79]
    if len(subset) < 2:
        return None
    subset.sort()
    for num in subset:
        if subset.count(num) > 1:
            subset.remove(num)
    if len(subset) < 2:
        return None
    return subset[1]