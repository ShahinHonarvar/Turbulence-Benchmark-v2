def find_second_smallest_num(numbers):
    if len(numbers) < 36:
        return None
    relevant_slice = numbers[32:36]
    if len(relevant_slice) < 2:
        return None
    sorted_slice = sorted(relevant_slice)
    return sorted_slice[1] if len(sorted_slice) > 1 else None