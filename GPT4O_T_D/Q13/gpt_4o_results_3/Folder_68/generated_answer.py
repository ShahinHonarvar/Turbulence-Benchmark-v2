def find_second_largest_num(numbers):
    if len(numbers) < 9:
        return None
    unique_numbers = list(set(numbers[:9]))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]