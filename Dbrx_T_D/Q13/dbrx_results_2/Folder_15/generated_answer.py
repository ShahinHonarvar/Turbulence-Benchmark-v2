def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 4:
        return None
    unique_numbers = list(set(numbers[:4]))
    unique_numbers.sort(reverse=True)
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[1]