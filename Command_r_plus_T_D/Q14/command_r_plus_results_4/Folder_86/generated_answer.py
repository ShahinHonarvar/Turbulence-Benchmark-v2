def find_second_smallest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    relevant_numbers = sorted(numbers[33:37])
    if len(relevant_numbers) < 2:
        return None
    else:
        return relevant_numbers[1]