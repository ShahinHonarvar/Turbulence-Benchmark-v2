def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    relevant_numbers = numbers[:9]
    unique_numbers = list(set(relevant_numbers))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort()
    return unique_numbers[-2]