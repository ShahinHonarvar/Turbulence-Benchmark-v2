def find_second_smallest_num(numbers):
    if len(numbers) < 9:
        return None
    sublist = numbers[4:9]
    unique_numbers = sorted(set(sublist))
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[1]