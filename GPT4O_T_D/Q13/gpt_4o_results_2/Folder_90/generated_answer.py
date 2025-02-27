def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) <= 746:
        return None
    sublist = numbers[262:747]
    if len(sublist) < 2:
        return None
    unique_numbers = set(sublist)
    if len(unique_numbers) < 2:
        return None
    unique_numbers.remove(max(unique_numbers))
    return max(unique_numbers)