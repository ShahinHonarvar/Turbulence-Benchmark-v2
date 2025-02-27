def find_second_smallest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    relevant_numbers = sorted(numbers[75:89])
    if len(relevant_numbers) < 2:
        return None
    return relevant_numbers[1]