def find_second_smallest_num(numbers):
    if len(numbers) < 73:
        return None
    sublist = numbers[31:73]
    if len(sublist) < 2:
        return None
    unique_numbers = sorted(set(sublist))
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[1]