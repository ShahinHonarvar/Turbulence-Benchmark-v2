def find_second_smallest_num(numbers):
    if len(numbers) < 9:
        return None
    sublist = numbers[6:9]
    if len(sublist) < 2:
        return None
    unique_numbers = set(sublist)
    if len(unique_numbers) < 2:
        return None
    sorted_numbers = sorted(unique_numbers)
    return sorted_numbers[1]