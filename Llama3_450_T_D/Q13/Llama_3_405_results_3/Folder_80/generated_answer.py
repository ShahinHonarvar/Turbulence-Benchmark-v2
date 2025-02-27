def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    relevant_numbers = numbers[64:67]
    sorted_numbers = sorted(relevant_numbers, reverse=True)
    if len(sorted_numbers) < 2:
        return None
    return sorted_numbers[1]