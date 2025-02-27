def find_second_largest_num(numbers):
    if len(numbers) < 89:
        return None
    sublist = numbers[22:89]
    if len(sublist) < 2:
        return None
    unique_numbers = set(sublist)
    if len(unique_numbers) < 2:
        return None
    unique_numbers.remove(max(unique_numbers))
    return max(unique_numbers)