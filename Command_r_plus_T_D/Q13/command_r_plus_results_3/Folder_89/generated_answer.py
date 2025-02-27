def find_second_largest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    relevant_numbers = numbers[56:83]
    relevant_numbers.sort()
    if len(relevant_numbers) < 2:
        return None
    return relevant_numbers[-2]