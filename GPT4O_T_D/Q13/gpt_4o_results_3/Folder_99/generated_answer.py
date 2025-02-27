def find_second_largest_num(numbers):
    if len(numbers) < 371:
        return None
    sublist = numbers[310:371]
    unique_numbers = set(sublist)
    if len(unique_numbers) < 2:
        return None
    unique_numbers = sorted(unique_numbers, reverse=True)
    return unique_numbers[1]