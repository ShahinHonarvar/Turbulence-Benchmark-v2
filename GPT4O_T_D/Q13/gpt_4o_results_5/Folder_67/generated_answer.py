def find_second_largest_num(numbers):
    if len(numbers) < 23:
        return None
    sublist = numbers[22:51]
    if len(sublist) < 2:
        return None
    unique_numbers = set(sublist)
    if len(unique_numbers) < 2:
        return None
    sorted_numbers = sorted(unique_numbers, reverse=True)
    return sorted_numbers[1]