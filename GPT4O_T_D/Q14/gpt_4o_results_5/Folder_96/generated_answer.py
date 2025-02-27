def find_second_smallest_num(numbers):
    if len(numbers) < 201:
        return None
    sublist = numbers[50:201]
    unique_sorted = sorted(set(sublist))
    if len(unique_sorted) < 2:
        return None
    return unique_sorted[1]