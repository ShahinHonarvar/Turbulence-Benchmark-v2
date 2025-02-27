def find_second_smallest_num(numbers):
    sublist = numbers[62:93]
    if len(sublist) < 2:
        return None
    unique_numbers = sorted(set(sublist))
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[1]