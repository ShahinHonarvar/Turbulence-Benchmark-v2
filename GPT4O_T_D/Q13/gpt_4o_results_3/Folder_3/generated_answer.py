def find_second_largest_num(numbers):
    if len(numbers) < 93:
        return None
    sublist = numbers[62:93]
    if len(sublist) < 2:
        return None
    unique_numbers = list(set(sublist))
    unique_numbers.sort(reverse=True)
    return unique_numbers[1] if len(unique_numbers) > 1 else None