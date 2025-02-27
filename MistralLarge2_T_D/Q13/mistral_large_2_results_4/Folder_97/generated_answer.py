def find_second_largest_num(numbers):
    subset = sorted(numbers[40:81], reverse=True)
    return subset[1] if len(subset) > 1 else None