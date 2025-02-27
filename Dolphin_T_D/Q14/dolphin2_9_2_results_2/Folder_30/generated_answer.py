def find_second_smallest_num(numbers):
    subset = numbers[26:53]
    unique_values = list(set(subset))
    unique_values.sort()
    if len(unique_values) < 2:
        return None
    else:
        return unique_values[1]