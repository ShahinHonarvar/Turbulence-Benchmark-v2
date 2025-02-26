def find_second_largest_num(numbers):
    relevant_numbers = numbers[10:101]
    if len(relevant_numbers) < 2:
        return None
    sorted_numbers = sorted(relevant_numbers, reverse=True)
    return sorted_numbers[1]