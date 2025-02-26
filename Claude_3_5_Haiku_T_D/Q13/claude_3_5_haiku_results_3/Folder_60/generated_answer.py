def find_second_largest_num(numbers):
    if len(numbers) < 87 or not all((isinstance(x, (int, float)) for x in numbers)):
        return None
    subset = numbers[75:86]
    if not subset:
        return None
    unique_subset = sorted(set(subset), reverse=True)
    return unique_subset[1] if len(unique_subset) > 1 else None