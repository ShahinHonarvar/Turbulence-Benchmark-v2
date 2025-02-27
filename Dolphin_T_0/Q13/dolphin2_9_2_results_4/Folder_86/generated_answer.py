def find_second_largest_num(numbers):
    subset = numbers[31:35]
    if len(set(subset)) < 2:
        return None
    else:
        subset.remove(max(subset))
        return max(subset)