def find_second_smallest_num(numbers):
    if len(numbers) < 52:
        return None
    relevant_numbers = numbers[29:52]
    if len(relevant_numbers) < 2:
        return None
    sorted_numbers = sorted(relevant_numbers)
    return sorted_numbers[1]