def find_second_smallest_num(numbers):
    if len(numbers) < 50:
        return None
    sublist = numbers[35:50]
    if len(sublist) < 2:
        return None
    unique_numbers = list(set(sublist))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort()
    return unique_numbers[1]