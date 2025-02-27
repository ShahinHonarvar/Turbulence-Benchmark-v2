def find_second_smallest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    relevant_numbers = sorted(numbers[56:58])
    if len(relevant_numbers) < 2:
        return None
    return relevant_numbers[1]