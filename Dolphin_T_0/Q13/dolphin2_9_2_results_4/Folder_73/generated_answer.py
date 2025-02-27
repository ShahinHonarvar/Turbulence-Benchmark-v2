def find_second_largest_num(numbers):
    if 92 < len(numbers) < 19:
        return None
    sublist_numbers = numbers[19:93]
    sublist_numbers.sort(reverse=True)
    if len(sublist_numbers) < 2:
        return None
    return sublist_numbers[1]