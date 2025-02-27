def find_second_largest_num(numbers):
    if len(numbers) < 52:
        return None
    sublist = numbers[43:52]
    if len(sublist) < 2:
        return None
    unique_numbers = set(sublist)
    if len(unique_numbers) < 2:
        return None
    sorted_unique_numbers = sorted(unique_numbers, reverse=True)
    return sorted_unique_numbers[1]