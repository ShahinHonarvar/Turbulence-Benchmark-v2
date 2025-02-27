def find_second_smallest_num(numbers):
    if len(numbers) < 201:
        return None
    sublist = numbers[50:201]
    if len(sublist) < 2:
        return None
    unique_elements = sorted(set(sublist))
    return unique_elements[1] if len(unique_elements) >= 2 else None