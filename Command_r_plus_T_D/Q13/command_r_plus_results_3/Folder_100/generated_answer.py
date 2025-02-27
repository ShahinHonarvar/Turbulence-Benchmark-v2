def find_second_largest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    if len(numbers) < 69:
        return None
    relevant_numbers = numbers[42:69]
    relevant_numbers.sort()
    if len(relevant_numbers) < 2:
        return None
    return relevant_numbers[-2]