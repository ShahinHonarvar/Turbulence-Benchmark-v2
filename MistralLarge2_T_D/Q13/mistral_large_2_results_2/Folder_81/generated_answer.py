def find_second_largest_num(numbers):
    if len(numbers) <= 100:
        subset = numbers[10:]
    else:
        subset = numbers[10:101]
    if len(subset) < 2:
        return None
    first_largest = max(subset)
    subset.remove(first_largest)
    second_largest = max(subset)
    return second_largest