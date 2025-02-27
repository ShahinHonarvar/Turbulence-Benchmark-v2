def find_second_smallest_num(numbers):
    if len(numbers) < 5:
        return None
    first_five = numbers[:5]
    unique_numbers = sorted(set(first_five))
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[1]