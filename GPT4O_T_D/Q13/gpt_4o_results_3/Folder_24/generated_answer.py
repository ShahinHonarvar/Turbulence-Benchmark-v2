def find_second_largest_num(numbers):
    if len(numbers) < 76:
        return None
    sublist = numbers[74:96]
    unique_numbers = set(sublist)
    if len(unique_numbers) < 2:
        return None
    return sorted(unique_numbers, reverse=True)[1]