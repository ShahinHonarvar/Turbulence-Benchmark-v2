def find_second_smallest_num(numbers):
    if len(numbers) < 3 or len(numbers[1:9]) < 2:
        return None
    relevant_numbers = numbers[1:9]
    sorted_numbers = sorted(set(relevant_numbers))
    return sorted_numbers[1] if len(sorted_numbers) >= 2 else None