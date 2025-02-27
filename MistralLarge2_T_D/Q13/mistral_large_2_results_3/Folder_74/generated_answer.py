def find_second_largest_num(numbers):
    if len(numbers) <= 78:
        subset = numbers[17:79]
    else:
        subset = numbers[17:78]
    if len(subset) < 2:
        return None
    first_largest = max(subset)
    subset.remove(first_largest)
    second_largest = max(subset)
    return second_largest