def find_second_largest_num(numbers):
    if len(numbers) < 33 or len(numbers[31:73]) < 2:
        return None
    subset = numbers[31:73]
    sorted_subset = sorted(subset, reverse=True)
    return sorted_subset[1]