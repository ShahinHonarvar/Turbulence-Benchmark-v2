def find_second_largest_num(numbers):
    unique_numbers = list(set(numbers[:4]))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]