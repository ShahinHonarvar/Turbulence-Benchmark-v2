def find_second_smallest_num(numbers):
    if len(numbers) < 85:
        return None
    sublist = numbers[70:85]
    if len(sublist) < 2:
        return None
    unique_numbers = list(set(sublist))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort()
    return unique_numbers[1]