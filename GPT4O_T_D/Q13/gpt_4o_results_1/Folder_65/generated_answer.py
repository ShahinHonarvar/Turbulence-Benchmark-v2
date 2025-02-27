def find_second_largest_num(numbers):
    if len(numbers) < 99:
        return None
    subrange = numbers[56:99]
    if len(subrange) < 2:
        return None
    unique_numbers = list(set(subrange))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]