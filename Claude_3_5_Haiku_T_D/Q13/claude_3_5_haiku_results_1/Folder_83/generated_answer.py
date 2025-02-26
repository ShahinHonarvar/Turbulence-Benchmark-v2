def find_second_largest_num(numbers):
    if not numbers or len(numbers) <= 1 or 90 >= len(numbers):
        return None
    sublist = numbers[90:91]
    if not sublist:
        return None
    return sorted(sublist, reverse=True)[1] if len(sublist) > 1 else None